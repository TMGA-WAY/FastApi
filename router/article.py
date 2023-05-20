from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import article_base, article_display
from db.databse import get_db
from db import db_article

router = APIRouter(
    prefix="/article",
    tags=["article"]
)


@router.post("/", response_model=article_display)
def create_article(request: article_base,
                   db: Session = Depends(get_db)) -> article_display:
    return db_article.create_article(db=db, request=request)


@router.get("/{id_}", response_model=article_display)
def get_article(id_: int, db: Session = Depends(get_db)) -> article_display:
    return db_article.get_article(db=db, id_=id_)
