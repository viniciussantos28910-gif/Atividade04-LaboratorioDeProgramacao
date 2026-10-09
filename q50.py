alunos = {}

for i in range(5):  # 0 1 2 3 4
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))

    alunos[nome] = nota

media = sum(alunos.values()) / len(alunos)
print("\n Media = ", media)
print("\n Alunos aprovados: ")

for nome, nota in alunos.items():
    if nota >= 7:
        print("Aluno aprovado: ", nome)
        print("\t Nota do aluno: ", nota)
