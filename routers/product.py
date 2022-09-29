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


# @router.get('/', response_model=List[schemas.ShowJean])
# def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return jean.get_all(db)


# @router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowJean)
# def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return jean.show(id, db)


# @router.post('/', status_code=status.HTTP_201_CREATED)
# def create(request: schemas.Jean, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return jean.create(request, db)


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destory(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return jean.destroy(id, db)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id: int, request: schemas.Jean, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return jean.update(id, request, db)

@router.get('/', response_class=HTMLResponse)
async def main(request: Request, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return view.main(request)


@router.get('/intro', response_class=HTMLResponse)
async def animation(request: Request):
    return view.animation(request, oauth2.login_check(request))

# @router.get('/shop', response_model=List[schemas.ShowProduct])


@router.get('/shop/')
@router.get('/shop/{category}', response_class=HTMLResponse)
@router.get('/shop/{category}/{pg}', response_class=HTMLResponse)
async def all(request: Request, category:str="top", pg: int = 1, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # return jean.get_all(db, pg)
    return view.products(request, product.get_all(db, current_user, category, pg), category, pg)


# @router.get('/shop-single',response_class=HTMLResponse)
# def about_jean(request:Request, pg: int =1,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
#     return view.about_products(request, products, pg)
