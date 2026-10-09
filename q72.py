def parse_cpf(cpf: str):

    try:
        int(cpf)
    except ValueError as erro:
        return f"ERRO: {erro}"
    else:
        return int(cpf)
