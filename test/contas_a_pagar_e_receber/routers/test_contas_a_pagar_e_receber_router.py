
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_deve_listar_contas_a_pagar_e_receber():
    response = client.get('/constas_apagar_e_receber')
    assert response.status_code == 200
    assert response.json() == (
        [{'id': 1, 'descricao': 'Aluguel', 'valor': '450', 'tipo': 'PAGAR'}, 
         {'id': 2, 'descricao': 'Luz', 'valor': '250', 'tipo': 'PAGAR'}, 
         {'id': 3, 'descricao': 'Aguá', 'valor': '70', 'tipo': 'PAGAR'}, 
         {'id': 4, 'descricao': 'Mercado', 'valor': '800', 'tipo': 'PAGAR'}, 
         {'id': 5, 'descricao': 'Internet', 'valor': '89', 'tipo': 'PAGAR'}, 
         {'id': 6, 'descricao': 'Cartão de credito', 'valor': '500', 'tipo': 'PAGAR'}, 
         {'id': 7, 'descricao': 'Salário', 'valor': '2000', 'tipo': 'RECEBER'}] 
    )
    

def test_deve_criar_contas_a_pagar_e_receber():
    nova_conta = {
        "descricao" : "Cursos da Alura",
        "valor": "1200",
        "tipo": "PAGAR"
    }
    nova_conta_copy = nova_conta.copy()
    
    nova_conta_copy["id"] = 8
    
    response = client.post("/constas_apagar_e_receber", json=nova_conta)
    assert response.status_code == 201
    assert response.json() == nova_conta_copy
