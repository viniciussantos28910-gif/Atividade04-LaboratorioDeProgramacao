def calcular_extremos(valores: list[float]) -> str:

    def maior(lista):
        return max(lista)

    def menor(lista):
        return min(lista)

    return f"Maximo: {maior(valores)}\n Minimo: {menor(valores)}"

numeros_colecao = [float(input("Digite um numero: ")) for contador in range(5)]

print(calcular_extremos(numeros_colecao))