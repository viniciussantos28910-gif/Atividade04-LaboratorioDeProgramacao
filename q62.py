def checar_numero(valor: int) -> str:
    soma_divisores = 0
    contador = 1

    while contador < valor:
        if valor % contador == 0:
            soma_divisores += contador
        contador += 1

    if checar_numero == valor:
        return True
    else:
        return False


usuario_entrada = int(input("Digite um valor inteiro: \n "))
resultado = checar_numero(usuario_entrada)

print(resultado)
