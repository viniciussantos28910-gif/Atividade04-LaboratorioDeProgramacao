catalogo = {}
for i in range(3):
    nome = input("Produto: ")
    preco = float(input("Valor: "))

    catalogo[nome] = preco

print(catalogo)