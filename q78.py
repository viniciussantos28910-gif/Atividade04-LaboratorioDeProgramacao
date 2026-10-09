import traceback

class OutOfRangeError(Exception):
    def __init__(self, message="As notas so vao de 0 a 10"):
        super().__init__(message)

def calcular_media(n1,n2,n3):
    def verif_length(num):
        if 0<= num <= 10:
            return True
        else:
            return False

    try:
        if any(not verif_length(float(x)) for x in [n1,n2,n3]):
            raise OutOfRangeError

    except (OutOfRangeError, TypeError, ValueError) as erro:
        print(erro)
        traceback.print_exc()
        return calcular_media(input("1° nota: "), input("2° nota: "), input("3° nota: "))

    else:
        lst = [float(x) for x in [n1,n2,n3]]
        return ("Aprovado" if sum(lst)/len(lst) >= 7 else "Reprovado")

print(calcular_media(3,4,5))
print(calcular_media("v","3", 1))