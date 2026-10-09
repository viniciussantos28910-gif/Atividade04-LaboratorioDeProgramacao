import requests

def try_get(id):

    try:
        resposta = requests.get(f"http://SiteFicticio.com/produto/{id}")
        prod_data = resposta.json()["preco"]
    except KeyError:
        print(f"Produto nao encontrado HTTP: 404")
    except Exception:
        print(f"Erro inesperado HTTP: 500")

try_get("1635")