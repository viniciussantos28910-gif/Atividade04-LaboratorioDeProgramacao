import random

sort_num = random.randint(1,10)
user_num = int(input("Numero: "))

if user_num is sort_num:
    print("Acertou!!")
else:
    print(f"O numero era {sort_num}")