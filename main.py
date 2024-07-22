import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def ola_sou_programador():
    return "Oi, eu sou programdor"