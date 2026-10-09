class Staff:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def registro(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "setor": self.setor
        }

nome = input("Nome: ")
idade = int(input("Idade: "))
setor = input("Setor de atuacao: ")

STAFF = Staff(nome, idade, setor)
registro = STAFF.registro()

for k, v in registro.items():
    print(f"{k}: {v}")