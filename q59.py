def numeros(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return min(n1, n2)
    return max(n1, n2)


n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

resultado = numeros(n1, n2)
print(f"Resultado: {resultado}")
