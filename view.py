from fastapi import Request
from typing import List
from fastapi.templating import Jinja2Templates
import schemas


templates = Jinja2Templates(directory="templates")


def signin(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


def select_taste(request: Request):
    return templates.TemplateResponse("preference.html", {"request": request})


def select_style(request: Request):
    return templates.TemplateResponse("style.html", {"request": request})


def animation(request: Request, login_check: bool):
    return templates.TemplateResponse("intro.html", {"request": request, "login_check": login_check})


def main(request: Request):
    return templates.TemplateResponse("zshop/index.html", {"request": request})


def products(request: Request, products: schemas.ShowProduct, category:str, pg: int):
    return templates.TemplateResponse("zshop/shop.html", {"request": request, "products": products, "category":category, "page": pg})


def about_product(request: Request, product: schemas.ShowProduct, reviews:schemas.ShowReview, relatedProducts:schemas.ShowProduct):
    return templates.TemplateResponse("zshop/shop-single.html", {"request": request, "product": product, "reviews":reviews, "relatedProducts":relatedProducts})


def reviews(request: Request, reviews: schemas.ShowReview, pg: int):
    return templates.TemplateResponse("zshop/shop-single.html", {"request": request, "reviews": reviews, "page": pg})
