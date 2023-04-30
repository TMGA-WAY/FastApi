import uvicorn
from fastapi import FastAPI
from rounter import blog_get

app = FastAPI()
app.include_router(blog_get.router)


@app.get('/')
def index():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run('main:app')
