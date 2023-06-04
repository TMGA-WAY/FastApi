from fastapi import APIRouter, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional

router = APIRouter(
    prefix="/product",
    tags=['product']
)

products = ['watch', 'camera', 'phone']


@router.get("/all")
def get_all_product() -> Response:
    data = " ".join(products)
    return Response(content=data, media_type='text/plain')


@router.get("/with_header")
def get_products(response: Response,
                 custom_header: Optional[str] = Header(None)):
    response.headers['custome_response_header'] = " and ".join(custom_header)
    return products


@router.get('/{id_}')
def get_product(id_: int):
    if id_ > len(products):
        out = "Product not available"
        return PlainTextResponse(content=out, media_type='text/plain')
    else:
        product = products[id_]
        out = f"""
        <head>
            <style>
                -product {{width:500px; height: 30px;
                 border: 2px inset green;
                 background-color : lightblue;
                 text-align: center}};
            </style>
        </head>
        <div class="product">{product} </div>
        """
        return HTMLResponse(content=out, media_type="text/html")
