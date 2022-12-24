import pandas as pd
import numpy as np
import json
from sklearn.neighbors import KNeighborsClassifier
import pymysql
import database
import models
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:throeld12!%40@127.0.0.1:3306/test?charset=utf8"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#db에서 데이터 가져오기
def get_data():

    global knn_clf_pants, knn_clf_top, json_pants, json_top, json_review_pants, json_review_top
    
    db = database.SessionLocal()

    top = db.query(models.Top)

    json_top = pd.read_sql(top.statement, top.session.bind)

    pants = db.query(models.Pants)

    json_pants = pd.read_sql(pants.statement, pants.session.bind)


    review_top = db.query(models.TopReview)

    json_review_top = pd.read_sql(review_top.statement, review_top.session.bind)

    review_pants = db.query(models.PantsReview)

    json_review_pants = pd.read_sql(review_pants.statement, review_pants.session.bind)

    json_top = json_top.fillna(3)
    json_pants = json_pants.fillna(3)

    #gender, height, weight를 x로 name을 y로 설정
    pants_x = json_review_pants.iloc[:,3:6]
    pants_y = json_review_pants['name']
    top_x = json_review_top.iloc[:,3:6]
    top_y = json_review_top['name']

    pants_x.loc[pants_x['gender'] == '남성', 'gender'] = 0
    pants_x.loc[pants_x['gender'] == '여성', 'gender'] = 1
    top_x.loc[top_x.gender == '남성', 'gender'] = 0
    top_x.loc[top_x.gender == '여성', 'gender'] = 1

    #knn 알고리즘 학습 
    knn_clf_pants = KNeighborsClassifier(n_neighbors=100)
    knn_clf_pants.fit(pants_x, pants_y)
    knn_clf_top = KNeighborsClassifier(n_neighbors=100)
    knn_clf_top.fit(top_x, top_y)

def knn_pants(gender, height, weight):

    get_data()

    if gender == '남성':
        gender = 0
    else :
        gender = 1

    sample = pd.DataFrame({'gender' : [gender], 'height' : [height], 'weight' : [weight]})
    near = knn_clf_pants.kneighbors(sample)[1][0][0:30]
    
    top_n = pd.DataFrame()
    for i in near:
        product_id = json_review_pants.product_id[i]
        temp = json_pants.loc[json_pants['product_id'] == product_id]
        if(len(temp) == 1):
            top_n = pd.concat([top_n, temp])
    
    top_n_list = top_n.to_dict('records')
    
    return top_n_list

def knn_top(gender, height, weight):

    get_data()

    if gender == '남성':
        gender = 0
    else :
        gender = 1

    sample = pd.DataFrame({'gender' : [gender], 'height' : [height], 'weight' : [weight]})
    near = knn_clf_top.kneighbors(sample)[1][0][0:30]
    
    top_n = pd.DataFrame()
    for i in near:
        product_id = json_review_top.product_id[i]
        temp = json_top.loc[json_top['product_id'] == product_id]
        if(len(temp) == 1):
            top_n = pd.concat([top_n, temp])
    
    top_n_list = top_n.to_dict('records')
    
    return top_n_list
    
if __name__ == "__main__":
    tr = knn_top('남성',185,82)
    pr = knn_pants('남성',185,82)
    for e in pr:
        print(e['product_id'])