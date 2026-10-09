import pathlib as pth


def checar_documento(caminho_arquivo: str):
    arquivo = pth.Path(caminho_arquivo)

    try:
        if not arquivo.exists():
            raise FileNotFoundError("Arquivo nao localizado...")
    except FileNotFoundError as falha:
        print(f"Alerta: {falha}")
    finally:
        print("Encerrando programa")


checar_documento("relatorio_vendas.txt")
