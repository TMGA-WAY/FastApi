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
