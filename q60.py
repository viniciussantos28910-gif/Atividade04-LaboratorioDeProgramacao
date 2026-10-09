def converter(temperatura_fahre):
    celsius = (5/9) * (temperatura_fahre - 32)
    return celsius


temp_fahre = float(input("Digite a temperatura em F:"))
temp_c = converter(temp_fahre)

print(f"{temp_fahre} em fahre equivale a {temp_c:.2f} em celcius")
