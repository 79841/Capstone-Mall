from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import models, schemas
from fastapi import HTTPException, status
from knn import knn_pants, knn_top
from fastapi import Depends
import oauth2

def get_all(db: Session, category:str, pg: int):
    if category == "top":
        products = db.query(models.Top)
    elif category == "pants":
        products = db.query(models.Pants)
    return products[(pg-1)*36+1:pg*36+1]

def get_one_product(db: Session, category:str, num: int):
    model = models.Top
    print(category)
    if category == "top":
        model = models.Top
    elif category == "pants":
        model = models.Pants
    return db.query(model).filter(model.product_id == num).first()

def show_recommend_list(db: Session, category:str, pg: int, current_user: schemas.User = Depends(oauth2.get_current_user)):
    print(current_user)
    user_info = db.query(models.User).filter(models.User.email == current_user.email).first().__dict__
    print(user_info)
    if category == "rtop":
        products = knn_top(user_info["gender"], user_info["height"], user_info["weight"])
    elif category == "rpants":
        products = knn_pants(user_info["gender"], user_info["height"], user_info["weight"])
    return products

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
