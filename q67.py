def validar_idade(valor: str) -> int:

    try:
        if int(valor) <= 0:
            raise ValueError
    except ValueError as excessao:
        print(f"Entrada invalida: {excessao}")
        return None
    else:
        return int(valor)


while True:
    entrada_usuario = input("Digite sua idade: ")

    if isinstance(validar_idade(entrada_usuario), int):
        print("Idade convertida")
        break
    else:
        print("Tente novamente")
