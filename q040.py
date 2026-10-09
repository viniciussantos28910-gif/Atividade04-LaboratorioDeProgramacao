import random

sort_num = random.randint(-500000)
user_num = int(input("numero: "))

if user_num > sort_num:
    print("O numero e menor que o que voce escolheu!!")
elif user_num < sort_num:
    print("O numero e maior que o que voce escolheu!!")
else:
    print("correto!!")