from typing import List
from fastapi import APIRouter, Depends, Request, status
import schemas, database, view, oauth2
from sqlalchemy.orm import Session
from repository import preference as p
from fastapi.responses import HTMLResponse, RedirectResponse


router = APIRouter(
    prefix='/preference',
    tags=['Preference']
)
get_db = database.get_db


@router.get('/', response_class=HTMLResponse)
async def select_taste(request: Request, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    if p.check_registered(db, current_user):
        return RedirectResponse(
        '/', status_code=status.HTTP_302_FOUND)
    return view.select_taste(request)


@router.post('/', response_class=RedirectResponse)
async def select_taste(preference: schemas.Preference = Depends(schemas.Preference.as_form), db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return p.select_taste(preference, db, current_user)


# @router.get('/', response_class=HTMLResponse)
# def select_style(request: Request):
#     return view.select_style(request)


# @router.post('/style', response_class=RedirectResponse)
# def select_style(request: schemas.Style = Depends(schemas.Style.as_form), db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return p.select_style(request, db, current_user)
