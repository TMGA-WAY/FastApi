from db.databse import base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean


class db_user(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
