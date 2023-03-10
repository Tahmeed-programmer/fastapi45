# main.py

from fastapi import FastAPI


from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Union

class Item2(BaseModel):
    text: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}

@app.post("/h5/")
def hello3(item:Item2):
    return {"message":" TutLinks.com"}

