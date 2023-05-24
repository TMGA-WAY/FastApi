import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from router import blog_get
from router import blog_post
from router import article
from db import models
from db.databse import engine
from router import user
from exception import StoryException

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)


@app.get('/')
def index():
    return {"message": "Hello World"}


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418,
                        content={'detail': exc.name})


models.base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run('main:app')
