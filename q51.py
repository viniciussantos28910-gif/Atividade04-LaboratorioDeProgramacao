temperatura = []
for i in range(5):
    temp = float(input("Digite a Temperatura: "))
    temperatura.append(temp)

media_temp = sum(temperatura)/len(temperatura)
print(f"A media das temperaturas e: {media_temp}")

if 18 <= media_temp <= 28:
    print("Temperatura Ideal pro cultivo")
else:
    print("Temperatura esta desfavoravel pro cultivo")

print(temperatura)
