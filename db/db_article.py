from schema import ArticleBase
from db.models import DbArticle
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from exception import StoryException


def create_article(db: Session, request: ArticleBase):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No story Please")
    article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_article(db: Session, id_: int):
    article = db.query(DbArticle).filter(DbArticle.id == id_).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id {1} not found')
    return article
