from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy import Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import oracle


class User(Base):
    __tablename__ = 'uinfo'

    id_seq = Sequence('USER_ID_SEQ', metadata=Base.metadata, minvalue=1001000)
    id = Column(Integer, Sequence('USER_ID_SEQ'), primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    # phonenumber = Column(String(100), nullable=False, unique=True)
    # birthday = Column(String(100))
    # age = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    # jeansize = Column(String(10))
    gender = Column(String(10))



class Pants(Base):
    __tablename__ = 'pants'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    brand = Column(String(200))
    hashtag = Column(String(200))
    rating = Column(Float)
    image = Column(String(200))
    price = Column(Integer)
    heart = Column(Integer)

class Top(Base):
    __tablename__ = 'top'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    brand = Column(String(200))
    hashtag = Column(String(200))
    rating = Column(Float)
    image = Column(String(200))
    price = Column(Integer)
    heart = Column(Integer)


class PantsReview(Base):
    __tablename__ = 'pants_reviews'

    review_id = Column(Integer,  primary_key=True)
    product_id = Column(Integer, ForeignKey('pants.product_id'))
    name = Column(String(300), nullable=False)
    gender = Column(String(10))
    height = Column(Integer)
    weight = Column(Integer)
    rating = Column(Float)
    size = Column(String(100))
    evl = Column(String(300))
    image = Column(String(1000))


class TopReview(Base):
    __tablename__ = 'top_reviews'

    review_id = Column(Integer,  primary_key=True)
    product_id = Column(Integer, ForeignKey('top.product_id'))
    name = Column(String(100), nullable=False)
    gender = Column(String(10))
    height = Column(Integer)
    weight = Column(Integer)
    rating = Column(Float)
    size = Column(String(100))
    evl = Column(String(300))
    image = Column(String(1000))
