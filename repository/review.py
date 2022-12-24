from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status


def get_all_review(db: Session, category:str, num: int):
    reviewModel = models.TopReview
    if category == "top":
        reviewModel = models.TopReview
    elif category == "pants":
        reviewModel = models.PantsReview
    result = db.query(reviewModel).filter(reviewModel.product_id == num)[0:3]

    return result


def get_one_product(db: Session, category:str, num: int):
    if category == "top":
        model = models.Top
    elif category == "pants":
        model = models.Pants
    return db.query(model).filter(model.product_id == num).first()


def get_related_products(db:Session, category:str, num: int):
    if category == "top":
        model = models.Top
    elif category == "pants":
        model = models.Pants
    return db.query(model).filter(model.product_id != num)[0:9]

def null_num(db: Session, num: int):
    product_id = db.query(models.Product.product_id).filter(
        models.Product.product_id == num)
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Jean with id {id} not found")
    return 'null_num'
