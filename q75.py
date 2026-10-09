import random


def conexao_mock(sempre_falha=False):
    if sempre_falha or random.random() < 0.7:
        raise ConnectionError("Erro na comunicacao com a API")
    return "Sessao estabelecida com exito"


def conectar_com_tentativas(sempre_falha=False):
    tentativas = 3

    for tentativa in range(1, tentativas + 1):
        try:
            resposta = conexao_mock(sempre_falha)
        except ConnectionError:
            print(f"Tentativa {tentativa} de {tentativas} falhou.")
        else:
            print(resposta)
            return resposta

    print("Aviso: limite de 3 tentativas atingido. Finalizando com seguranca.")
    return None


print("Conexao instavel (aleatoria)")
conectar_com_tentativas()

print("Conexao que sempre falha")
conectar_com_tentativas(sempre_falha=True)
