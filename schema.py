from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    user_name: str
    email: str
    password: str


class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserDisplay(BaseModel):
    user_name: str
    email: str
    items: List[Article] = []

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class User(BaseModel):
    id: int
    user_name: str

    class Config:
        orm_mode = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True
