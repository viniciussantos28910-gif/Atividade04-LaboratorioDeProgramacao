num = int(input("Digite um numero inteiro positivo:"))
resultado = 1

for i in range(1, num + 1):
    resultado = resultado * i

print(f"O resultado do fatorial de {num} e: {resultado}")
