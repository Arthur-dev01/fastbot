import requests
import json

link_test = "https://webhook.site/33ed8010-98e2-424b-b2dc-6690d5c64ccc"

dados = {
    "Nome": "Ajuara",
    "Número": 5586991095131,
    "Mensagem:": "Olá, mundo!"
}

dados_json = json.dumps(dados)

requests.post(link_test, dados_json)


# Teste realizado através: https://webhook.site/#!/
