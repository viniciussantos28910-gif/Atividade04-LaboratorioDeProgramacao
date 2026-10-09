import random as rdm

class ExceptionSaldoInsuficiente(Exception):
    def __init__(self, message="Saldo insuficiente..."):
        self.message = message
        super().__init__(self.message)

class ExceptionUsuarioNaoEncontrado(Exception):
    def __init__(self, message="Usuario nao encontrado"):
        super().__init__(self.message)    

class User:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.id = str(rdm.randint(10000,99999))
        self.codigo = 0

    def __repr__(self):
        return self.id

class Banco:
    users = []

    def add_user(self):
        nome = input("Digite o nome de usuario: ")
        usuario = User(nome)
        usuario.codigo = len(self.users)
        self.users.append(usuario)
        
    def add_saldo(self,):
        index = input("Codigo do usuario: ")
        valor = input("Valor de deposito: ")

        try:
            int(index)
            float(valor)
        except ValueError:
            print("ERRO: parametros invalidos")
        else:
            index = int(index)
            valor = float(valor)
        
        self.users[index].saldo += valor

    def saque(self):
        index = input("Codigo do usuario: ") 
        valor = input("Valor do saque: ")

        try:
            if float(valor) > self.users[int(index)].saldo:
                raise ExceptionSaldoInsuficiente
            
        except ExceptionSaldoInsuficiente as erro:
            print(f"ERRO: {erro}")
            return self.saque()
        
        except ValueError:
            print(f"ERRO: Parametro invalido")
            return self.saque()
        
        else:
           valor =  float(valor)
           index = int(index)

        self.users[index].saldo -= valor

    def get_sumary(self):
        index = input("Codigo do uduario: ")

        try:
            int(index)
        except ValueError:
            print("Entrada invalida")
        else:
            index = int(index)
        for k, v in vars(self.users[index]).items():
            print(f"{k}: {v}")

    def get_users(self):
        for user in self.users:
            print(user)



Itau = Banco()
Itau.add_user()
Itau.get_users()
Itau.get_sumary()
Itau.add_saldo()
Itau.saque()
Itau.get_sumary()