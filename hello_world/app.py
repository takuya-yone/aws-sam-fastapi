from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(docs_url='/docs',
              #   openapi_url='/openapi.json',
              openapi_prefix="/Prod"
              )


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


lambda_handler = Mangum(app, lifespan="off")
