import traceback

class ErroSaldoInsuficiente(Exception):
    def __init__(self, message="Saldo insuficiente"):
        self.message = message
        super().__init__(self.message)

def realizar_saque(saldo, valor_saque):

    try:
        float(saldo)
        float(valor_saque)

        if float(valor_saque) < 0:
            raise ValueError("Valor de saque invalido")
        elif float(saldo) < float(valor_saque):
            raise ErroSaldoInsuficiente

    except (ValueError, ErroSaldoInsuficiente, TypeError) as erro:
        print(erro)
        traceback.print_exc()
        return realizar_saque(input("Digite as informacoes novamente:\nSaldo --> "),input("Valor do saque --> "))

    else:
        return float(saldo) - float(valor_saque)

print(realizar_saque(150, 35))
print(realizar_saque("ad4", 35))