from sqlalchemy.orm import Session
import models, schemas, hashing
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse


# def select_taste(request: schemas.Preference, db: Session, current_user: schemas.User):
#     user_taste = dict(request)
#     user_taste.update(userid=current_user.id)
#     user_taste = models.UserTaste(**user_taste)
#     db.add(user_taste)
#     db.commit()
#     db.refresh(user_taste)
#     return RedirectResponse(
#         '/choice/style', status_code=status.HTTP_302_FOUND)

def check_registered(db: Session, current_user: schemas.User):
    registered = db.query(models.Preference.userid).filter(models.Preference.userid == current_user.id).first()
    if registered:
        return True


def select_taste(preference: schemas.Preference, db: Session, current_user: schemas.User):

    user_taste = dict(preference)
    agegroup = db.query(models.User.agegroup).filter(models.User.id == current_user.id).first()

    user_taste.update(userid=current_user.id, a_agegroup=agegroup['agegroup'])

    user_taste = models.Preference(**user_taste)
    db.add(user_taste)
    db.commit()
    db.refresh(user_taste)

    # user_style = dict(style)
    # user_style.update(userid=current_user.id)
    # user_style = models.Style(**user_style)
    # db.add(user_style)
    # db.commit()
    # db.refresh(user_style)
    return RedirectResponse(
        '/intro', status_code=status.HTTP_302_FOUND)
