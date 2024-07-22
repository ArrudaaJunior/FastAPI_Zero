import uvicorn
from fastapi import FastAPI

from constas_apagar_e_receber.routers.contas_a_pagar_e_receber_router import router


app = FastAPI()


@app.get("/")
def ola_sou_programador():
    return "Oi, eu sou programdor"

app.include_router(router)