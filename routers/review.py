from typing import List, Optional
from fastapi import APIRouter, Depends, status, Request
import schemas, database, oauth2, view
from sqlalchemy.orm import Session
from repository import review
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix='/review',
    tags=['reviews']
)
get_db = database.get_db


# @router.get('/', response_class=HTMLResponse)
# async def main(request: Request, current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return view.main(request)



# @router.get('/shop-single',response_class=HTMLResponse)
# def all_review(request:Request, num: Optional[int]=None, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
# return view.reviews(request, review.get_all_review(db, num), num)


# @router.get('/shop-single',response_class=HTMLResponse)
# def one_product(request:Request, num: Optional[int]=None, db:Session=Depends(get_db) ,current_user: schemas.User = Depends(oauth2.get_current_user)):
# return view.single_products(request, review.get_one_product(db, num), num)


# @router.get('/shop-single', response_class=HTMLResponse)
# @router.get('/shop-single/{category}/{num}')
# async def product(request: Request, category:str, num: Optional[int] = None, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return view.about_product(request, review.get_one_product(db, category, num), review.get_all_review(db, category, num), review.get_related_products(db, category, num))


@router.get('/shop-single/{category}/{num}')
# async def product(request: Request, category:str, num: Optional[int] = None, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
async def product(request: Request, category:str, num: Optional[int] = None, db: Session = Depends(get_db)):
    return review.get_all_review(db, category, num)
