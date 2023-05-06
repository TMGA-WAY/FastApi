from fastapi import APIRouter, status, Response, Depends
from typing import Optional
from rounter.blog_post import required_functionalities
from enum import Enum

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)


@router.get('/all')
def get_all_blogs(page: int, page_size: Optional[int] = None,
                  req_parameter: dict = Depends(required_functionalities)):
    return {'message': f'all{page_size} blogs on page {page}',
            'req': req_parameter}


@router.get('/{id}/comments/{comment_id}', tags=['comments'])
def get_comment(id: int, comment_id: int, valid: bool = True,
                username: Optional[str] = None):
    return {'message': f'blog_id {id}, comments_id {comment_id},valid {valid},username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}


@router.get("/{id1}", status_code=status.HTTP_200_OK)
def get_blog(id1: int, response: Response):
    if id1 > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'{id1} not found'}
    else:
        return {"message": f"Blog with id {id1}"}
