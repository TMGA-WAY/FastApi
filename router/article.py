from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema import ArticleBase
from db.databse import get_db
from db import db_article
from auth.oauth2 import oauth2_schema, get_current_user
from schema import UserBase

router = APIRouter(
    prefix="/article",
    tags=["article"]
)


@router.post("/", response_model=ArticleBase)
def create_article(request: ArticleBase,
                   db: Session = Depends(get_db)) -> ArticleBase:
    return db_article.create_article(db=db, request=request)


@router.get("/{id_}")  # , response_model=ArticleBase)
def get_article(id_: int, db: Session = Depends(get_db),
                current_user: UserBase = Depends(get_current_user)):
    return {
        'data': db_article.get_article(db, id_),
        'current_user': current_user
    }
