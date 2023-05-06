from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


class BlogModel(BaseModel):
    title: str
    contact: str
    published: Optional[bool]


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }


@router.post("new/{id}/comment")
def create_comment(blog: BlogModel, id: int,
                   comment_id: int = Query(None,
                                           title="ID of the comment",
                                           description="Some description"),
                   content: str = Body(Ellipsis, min_length=10),
                   v: Optional[List[str]] = Query(None)):
    return {
        'id': id,
        'blog': blog,
        'comment_id': comment_id,
        'content': content,
        'v': v
    }


def required_functionalities():
    return {'message': 'Learning FastAPI is Important'}
