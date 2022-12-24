# from ctypes import WinError
from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class PantsBase(BaseModel):
    title: str
    body: str


class Pants(PantsBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    username: str
    email: str
    password: str
    # phonenumber: str
    # birthday: str
    gender:str
    height: int
    weight: int
    # jeansize: str
    


class CreateUser(User):
    passwordCheck:str

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        passwordCheck: str = Form(...),
        phonenumber: str = Form(...),
        birthday: str = Form(...),
        gender: str = Form(...),
        height: str = Form(...),
        weight: str = Form(...),
        jeansize: str = Form(...)
    ):
        return cls(username=username, email=email, password=password, passwordCheck=passwordCheck, phonenumber=phonenumber, birthday=birthday, gender=gender, height=int(height), weight=int(weight), jeansize=jeansize)


class ShowUser(BaseModel):
    username: str
    email: str
    pants: List[Pants] = []

    class Config():
        orm_mode = True


# class ShowJean(Jean):
#     buyer: ShowUser

#     class Config():
#         orm_mode = True

class ShowProduct(BaseModel):
    product_id: int
    name: str
    brand: str
    hashtag: Optional[str] = None
    rating: Optional[float] = None
    image: str
    price: int
    heart: int

    class Config():
        orm_mode = True

class ShowReview(BaseModel):
    review_id = int
    product_id = int
    name = str
    gender = str
    height = int
    weight = int
    rating = float
    size = str
    evl = str
    image = str
    
    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str

    @classmethod
    def as_form(
        cls,
        email: str = Form(...),
        password: str = Form(...)
    ):
        return cls(email=email, password=password)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None


class Preference(BaseModel):
    trend: int
    agegroup: int
    rating: int

    @classmethod
    def as_form(
        cls,
        trend: str = Form(...),
        agegroup: str = Form(...),
        rating: str = Form(...)
    ):
        return cls(trend=(4-int(trend)), agegroup=(4-int(agegroup)), rating=(4-int(rating)))


class Style(BaseModel):
    wide: float
    slim: float
    tapered: float
    crop: float

    @classmethod
    def as_form(
        cls,
        wide: str = Form(...),
        slim: str = Form(...),
        tapered: str = Form(...),
        crop: str = Form(...)
    ):
        return cls(wide=float(wide), slim=float(slim), tapered=float(tapered), crop=float(crop))
