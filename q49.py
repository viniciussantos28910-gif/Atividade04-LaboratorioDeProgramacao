registro = {}

def add_aluno():
    nome = input("Nome: ")
    nota = float(input("Nota: "))

    registro[nome] = nota
    print(" sucesso!!")

def get_alunos():
    for k, v in registro.items():
        print(f"{k}: {v}")

while True:
    act = input(" [1: adicionar aluno, 2: ver registro, 3: sair]")

    match act:
        case "1":
            add_aluno()
        case "2":
            get_alunos()
        case "3":
            break
        case _:
            print(" invalido")