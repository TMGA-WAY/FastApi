from fastapi import APIRouter, Depends
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
