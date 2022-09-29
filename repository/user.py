from sqlalchemy.orm import Session
import models, schemas, hashing
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
import datetime

def create(request: schemas.CreateUser, db: Session):

    user = dict(request)
    if user['password'] != user['passwordCheck']:
        return 'password not correct'
    user.update(password=hashing.Hash.bcrypt(user['password']))
    
    user.pop("passwordCheck")

    new_user = models.User(**user)
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return RedirectResponse(
        '/auth', status_code=status.HTTP_302_FOUND)


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    return user
