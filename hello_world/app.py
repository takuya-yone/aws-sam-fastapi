from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(
              root_path="/Prod"
              )

@app.on_event("startup")
def startup_event():
    # print("startup_event")
    return None

@app.on_event("shutdown")
def shutdown_event():
    # print("shutdown_event")
    return None

@app.get("/")
def read_root():
    return {"Hello": "Root"}

@app.get("/hello")
def read_hello():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


lambda_handler = Mangum(app, lifespan="auto")
