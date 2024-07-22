from decimal import Decimal
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/constas_apagar_e_receber")

class ContaPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str # PAGAR, RECEBER

class ContaPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str # PAGAR, RECEBER

@router.get("", response_model=List[ContaPagarReceberResponse])
def listar_contas():
    return [
        ContaPagarReceberResponse(
            id=1,
            descricao="Aluguel",
            valor=450,
            tipo="PAGAR"
        ),
        ContaPagarReceberResponse(
            id=2,
            descricao="Luz",
            valor=250,
            tipo="PAGAR"
        ),
        ContaPagarReceberResponse(
            id=3,
            descricao="Aguá",
            valor=70,
            tipo="PAGAR"
        ),
        ContaPagarReceberResponse(
            id=4,
            descricao="Mercado",
            valor=800,
            tipo="PAGAR"
        ),
        ContaPagarReceberResponse(
            id=5,
            descricao="Internet",
            valor=89,
            tipo="PAGAR"
        ),
        ContaPagarReceberResponse(
            id=6,
            descricao="Cartão de credito",
            valor=500,
            tipo="PAGAR"
        ),
        ContaPagarReceberResponse(
            id=7,
            descricao="Salário",
            valor=2000,
            tipo="RECEBER"
        )
    ]
    

@router.post("", response_model=ContaPagarReceberResponse, status_code=201)
def criar_conta(conta: ContaPagarReceberRequest):
    return ContaPagarReceberResponse(
        id=8,
        descricao=conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )