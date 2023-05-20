import uvicorn
from fastapi import FastAPI
from router import blog_get
from router import blog_post
from db import models
from db.databse import engine
from router import user

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)


@app.get('/')
def index():
    return {"message": "Hello World"}


models.base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run('main:app')
