total = 0

while True:
    valor = input("Digite um valor (ou digite 0 para sair): ")

    if valor == "0":
        break
    total += float(valor)

print(f"A soma dos valores foi {total}")
