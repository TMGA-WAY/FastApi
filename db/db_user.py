from sqlalchemy.orm.session import Session
from schema import user_base
from db.models import db_user
from db.hash import hash_user


def create_user(db: Session, request: user_base):
    new_user = db_user(
        user_name=request.user_name,
        email=request.email,
        password=hash_user.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    return db.query(db_user).all()


def get_user(db: Session, id_: int):
    return db.query(db_user).filter(db_user.id == id_).first()


def update_user(db: Session, id_: int, request: user_base):
    user = db.query(db_user).filter(db_user.id == id_)
    user.update({
        db_user.user_name: request.user_name,
        db_user.email: request.email,
        db_user.password: hash_user.bcrypt(request.password)
    })
    db.commit()
    return 'ok'
