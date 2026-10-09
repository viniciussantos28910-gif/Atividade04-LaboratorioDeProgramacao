n_prod = int(input("N° de produtos: "))
lst = [input("Produto: ") for i in range(n_prod)]
for i, e in enumerate(lst):
    print(f"{i+1}. {e}")