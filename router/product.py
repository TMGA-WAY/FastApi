from fastapi import APIRouter
from fastapi.responses import Response, HTMLResponse

router = APIRouter(
    prefix="/product",
    tags=['product']
)

products = ['watch', 'camera', 'phone']


@router.get("/all", response_model=Response)
def get_all_product() -> Response:
    data = " ".join(products)
    return Response(content=data, media_type='text/plain')


@router.get('/{id_}')
def get_product(id_: int) -> HTMLResponse:
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
