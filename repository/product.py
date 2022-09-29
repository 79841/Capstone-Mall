from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import models, schemas
from fastapi import HTTPException, status


# def get_all(db: Session):
#     return db.query(models.Pants).all()


def get_all(db: Session, current_user: schemas.User, category:str, pg: int):
    if category == "top":
        products = db.query(models.Top)
    elif category == "pants":
        products = db.query(models.Pants)
    # return len(list(r))

    return products[(pg-1)*10+1:pg*10+1]
    # return db.query(models.Product).all()[(pg-1)*10+1:pg*10+1]
    # return db.query(models.Product).all()


def show(id: int, db: Session):
    pants = db.query(models.Pants).filter(models.Pants.id == id).first()
    if not pants:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pants with the id {id} is not available")
    return pants


def create(request: schemas.Pants, db: Session):
    new_pants = models.Pants(title=request.title, body=request.body, user_id=3)
    db.add(new_pants)
    db.commit()
    db.refresh(new_pants)
    return new_pants


def destroy(id: int, db: Session):
    pants = db.query(models.Pants).filter(models.Pants.id ==
                                        id)
    if not pants.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"pants with id {id} not found")
    pants.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Pants, db: Session):
    pants = db.query(models.Pants).filter(models.Pants.id ==
                                        id)
    if not pants.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pants with id {id} not found")
    pants.update(dict(request))
    db.commit()
    return 'updated'
