try:
    lucros = float(input("Digite o valor dos lucros:"))
    acionista = int(input("Digite a quantidade de acionistas:"))

    resultado = lucros / acionista
    print(f"Lucro acionista: {resultado:.2f}")


except ZeroDivisionError as erro:
    print("Erro: A quantidade de acionistas nao piode ser zero")

except ValueError:
    print("Erro: Digite valores numericos validos.")
