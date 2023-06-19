from fastapi import APIRouter, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional, List, Dict

router = APIRouter(
    prefix="/product",
    tags=['product']
)

products = ['watch', 'camera', 'phone']


@router.post("/new")
def create_product(name: str = Form(...)) -> List[str]:
    products.append(name)
    return products


@router.get("/all")
def get_all_product() -> Response:
    data = " ".join(products)
    response = Response(content=data, media_type='text/plain')
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get("/with_header")
def get_products(response: Response,
                 custom_header: Optional[str] = Header(None),
                 test_cookie: Optional[str] = Cookie(None)) -> Dict:
    response.headers['custom_response_header'] = " and ".join(custom_header)
    return {"data": products, "custom_header": custom_header, "cookie": test_cookie}


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
