from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
def root(name: str):
    return {"name": name}


@app.get("/home-err/{name}")
def home(name: int):
    return {"name": name}
