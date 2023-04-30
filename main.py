import uvicorn
from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return {"message": "Hello World"}


@app.get('/blog/all', tags=['blog'])
def get_all_blogs(page: int, page_size: Optional[int] = None):
    return {'message': f'all{page_size} blogs on page {page}'}


@app.get('/blog/{id}/comments/{comment_id}', tags=['blog','comments'])
def get_comment(id: int, comment_id: int, valid: bool = True,
                username: Optional[str] = None):
    return {'message': f'blog_id {id}, comments_id {comment_id},valid {valid},username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}


@app.get("/blog/{id1}", status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id1: int, response: Response):
    if id1 > 5:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'error': f'{id1} not found'}
    else:
        return {"message": f"Blog with id {id1}"}


if __name__ == '__main__':
    uvicorn.run('main:app')
