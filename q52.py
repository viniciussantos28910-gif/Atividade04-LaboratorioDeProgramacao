estoque = {}
for i in range(5):
    nome_medicamento = input("Nome do medicamento: ")
    quantidade = int(input("Quantidade:"))
    estoque[nome_medicamento] = quantidade

buscar = input("Qual medicamento voce esta buscando: ")

if buscar in estoque:
    print("Tem", estoque[buscar], "unidades do medicamento", buscar, "no estoque")
else:
    print("Medicamento não encontrado.")
