from typing import List
from fastapi import APIRouter, Depends, status, Request
import schemas, database, oauth2, view
from sqlalchemy.orm import Session
from repository import product, authentication as auth
from fastapi.responses import HTMLResponse

router = APIRouter(
    # prefix="/",
    tags=['products']
)
get_db = database.get_db


@router.get('/product/{category}/{id}')
async def all(request: Request, category:str="top", id: int = 1, db: Session = Depends(get_db)):
   return product.get_one_product(db, category, id)

@router.get('/shop/')
@router.get('/shop/{category}')
@router.get('/shop/{category}/{pg}')
async def all(request: Request, category:str="top", pg: int = 1, db: Session = Depends(get_db)):

    return product.get_all(db, category, pg)

@router.get('/recommend/')
@router.get('/recommend/{category}')
@router.get('/recommend/{category}/{pg}')
async def all(request: Request, category:str="top", pg: int = 1, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return product.show_recommend_list(db, category, pg, current_user)
