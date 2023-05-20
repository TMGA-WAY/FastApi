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
def create_user(request: user_base, db: Session = Depends(get_db)) -> user_display:
    return db_user.create_user(db=db, request=request)


@router.get('/', response_model=List[user_display])
def get_all_user(db: Session = Depends(get_db)) -> List[user_display]:
    return db_user.get_all(db)


@router.get("/{id_}", response_model=user_display)
def get_user(id_: int, db: Session = Depends(get_db)) -> user_display:
    return db_user.get_user(db=db, id_=id_)


@router.post("/{id}/update")
def update_user(id_: int, request: user_base,
                db: Session = Depends(get_db)) -> str:
    return db_user.update_user(db=db, id_=id_, request=request)


@router.delete("/{id}/delete")
def user_delete(id_: int, db: Session = Depends(get_db)) -> str:
    return db_user.delete_user(db=db, id_=id_)
