from fastapi import APIRouter, Depends
from typing import List
from schema import user_base
from sqlalchemy.orm import Session
from db.databse import get_db
from db import db_user
from schema import user_display

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# create user
@router.post('/', response_model=user_display)
def create_user(request: user_base, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get('/', response_model=List[user_display])
def get_all_user(db: Session = Depends(get_db)):
    return db_user.get_all(db)


@router.get("/{id_}", response_model=user_display)
def get_user(id_: int, db: Session = Depends(get_db)):
    return db_user.get_user(db=db, id_=id_)
