from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, Field


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if (model_name is ModelName.alexnet):
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if (model_name.value == "lenet"):
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/{name}")
def root(name: str):
    return {"name": name}


@app.get("/home-err/{name}")
def home(name: int):
    return {"name": name}


# 쿼리 스트링 예제
fake_items_db = [{"item_name": "Foo"}, {"item_name", "Bar"}, {"item_name", "Baz"}]


@app.get("/items/{item_id}")
def read_item(item_id: int, page: int = 0, size: int = 10):
    return fake_items_db[page: page + size]


# post 예제
@app.post("/")
def home_post(msg: str):
    return {"Hello": "POST", "msg": msg}


class DataInput(BaseModel):
    name: str


@app.post("/")
def home_post(data_request: DataInput):
    return {"Hello": "POST", "msg": data_request.name}
