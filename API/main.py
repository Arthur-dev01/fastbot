from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MensagemModel(BaseModel):
    msg: str


@app.get("/")
def test():
    data = {
        "msg": "Hello, world!"
    }
    return data
