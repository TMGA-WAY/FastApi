import shutil

from fastapi import APIRouter, File
from fastapi.datastructures import UploadFile
from fastapi.responses import FileResponse

router = APIRouter(
    prefix='/file',
    tags=['file']
)


@router.post("/file")
def get_file(file: bytes = File(...)):
    content = file.decode('UTF-8')
    line = content.split('\n')
    return {'lines': line}


@router.post('/uploadFile')
def get_upload_file(upload_file: UploadFile = File(...)):
    path = f"files/{upload_file.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {
        'file name': upload_file.filename
    }


@router.get("/download/{name}", response_class=FileResponse)
def get_file(name: str):
    path = f'files/{name}'
    return path
