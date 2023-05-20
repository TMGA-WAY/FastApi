from pydantic import BaseModel


class user_base(BaseModel):
    user_name: str
    email: str
    password: str


class user_display(BaseModel):
    user_name: str
    email: str

    class Config:
        orm_mode = True
