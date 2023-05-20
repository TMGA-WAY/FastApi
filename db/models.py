from db.databse import base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class db_user(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("db_article", back_populates="user")


class db_article(base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("db_user", back_populates="items")
