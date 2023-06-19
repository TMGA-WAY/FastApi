import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from db import models
from db.databse import engine
from router import user, article, product, blog_get, blog_post
from exception import StoryException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


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


origin = "http://localhost:3000"

models.base.metadata.create_all(engine)
app.add_middleware(
    CORSMiddleware,
    allow_origin=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run('main:app')
