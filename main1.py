# main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}

@app.get("/h5")
def hello():
    return {"message":" TutLinks.com"}

