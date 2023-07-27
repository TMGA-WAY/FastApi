from sqlalchemy.orm.session import Session
from schema import UserBase
from db.models import DbUser
from db.hash import HashUser
from fastapi import HTTPException, status


def create_user(db: Session, request: DbUser):
    new_user = DbUser(
        user_name=request.user_name,
        email=request.email,
        password=HashUser.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    print("inside get_all")
    return db.query(DbUser).all()


def get_user(db: Session, id_: int):
    user = db.query(DbUser).filter(DbUser.id == id_)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id_} not found')
    return user


def update_user(db: Session, id_: int, request: DbUser):
    user = db.query(DbUser).filter(DbUser.id == id_)
    user.update({
        DbUser.user_name: request.user_name,
        DbUser.email: request.email,
        DbUser.password: HashUser.bcrypt(request.password)
    })
    db.commit()
    return 'ok'


def delete_user(db: Session, id_: int):
    user = db.query(DbUser).filter(DbUser.id == id_).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id_} not found')
    db.delete(user)
    db.commit()
    return "ok"


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.user_name == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found')
    return user
