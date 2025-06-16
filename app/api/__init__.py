from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados esperado
class Modelo_Mensagem(BaseModel):
    msg: str


@app.post("/webhook")
async def receber_dados(data: Modelo_Mensagem):
    print(f"DADOS RECEBIDOS: {data}")
    return {
        "status": "Sucesso",
        "recebido": data.msg
    }
    
