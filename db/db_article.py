from schema import article_base
from db.models import db_article
from sqlalchemy.orm.session import Session


def create_article(db: Session, request: article_base):
    article = db_article(
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
    article = db.query(db_article).filter(db_article.id == id_).first()
    return article
