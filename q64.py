def soma_espe(a, b, c):
    soma = a + b + c
    if soma <= 21:
        return soma
    
    if 11 in (a, b, c):
        soma -= 10

    if  soma > 21:
        return -1

    return soma

print(soma_espe(5, 5, 11))  