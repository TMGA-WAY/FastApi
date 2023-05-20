from pydantic import BaseModel
from typing import List


class user_base(BaseModel):
    user_name: str
    email: str
    password: str


class article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class user_display(BaseModel):
    user_name: str
    email: str
    items: List[article] = []

    class Config:
        orm_mode = True


class article_base(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class user(BaseModel):
    id: int
    user_name: str

    class Config:
        orm_mode = True


class article_display(BaseModel):
    title: str
    content: str
    published: bool
    user: user

    class Config:
        orm_mode = True
