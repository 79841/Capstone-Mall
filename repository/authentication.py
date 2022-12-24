from typing import Optional
from fastapi import Depends, status, HTTPException, Header, Request
import schemas, database, models, getToken
from sqlalchemy.orm import Session
from hashing import Hash
from fastapi.responses import RedirectResponse
from fastapi.security.utils import get_authorization_scheme_param


def signin(request: schemas.Login, db: Session = Depends(database.get_db)):
    print(request.email)
    user = db.query(models.User).filter(
        models.User.email == request.email).first()
    print(user.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = getToken.create_access_token(
        data={"id": user.id, "email": user.email})
    print(access_token)
    # response = RedirectResponse(
    #     '/', status_code=status.HTTP_302_FOUND)
    # response.set_cookie(
    #     "Authorization",
    #     value=f"Bearer {access_token}",
    #     httponly=True,
    #     max_age=1800,
    #     expires=1800,
    # )
    # return response
    return {"Authorization":f"Bearer {access_token}"}


def logout():
    response = RedirectResponse(url="/auth")
    response.delete_cookie("Authorization")
    return response
