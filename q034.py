registro = {}
num_student = int(input("numero de estudantes: "))

for i in range(num_student):
    nome = input("nome do aluno: ")
    nota = float(input("nota: "))
    registro[nome] = nota

query = input("nome do aluno : ")
if query in registro:
    print(registro[query])
else:
    print("inexistente")