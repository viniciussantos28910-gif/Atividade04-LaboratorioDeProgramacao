quadrado = 0
graos = 1
soma = 0

while quadrado <= 63:
    quadrado = quadrado + 1
    if quadrado > 1:
        graos = graos * 2
        soma = soma + graos
    print("\n Quadrado ", quadrado, " tem ", graos, " graos ")
