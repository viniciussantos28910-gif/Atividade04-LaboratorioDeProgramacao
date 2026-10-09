lst = []

while True:
    n_livros = input("Digite a quantidade de livros  pela turma [Deixe vazio para terminar]: ")
    if not n_livros:
        break
    lst.append(float(n_livros))

print(max(lst))