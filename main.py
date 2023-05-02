import uvicorn
from fastapi import FastAPI
from rounter import blog_get
from rounter import blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run('main:app')
