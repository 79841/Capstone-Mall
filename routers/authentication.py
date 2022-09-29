from typing import Optional
from fastapi import APIRouter, Depends, Request, Header
import schemas, database, view, oauth2
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, Response, RedirectResponse
from repository import authentication as auth


router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)


@router.get('/', response_class=HTMLResponse)
async def signin(request: Request):
    if oauth2.login_check(request):
        return RedirectResponse(url="/")

    return view.signin(request)


@ router.post('/', response_class=Response)
async def signin(request: schemas.Login = Depends(schemas.Login.as_form), db: Session = Depends(database.get_db)):
    return auth.signin(request, db)


@ router.get("/logout")
async def logout():
    return auth.logout()
