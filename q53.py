import random

participantes = ["Ana", "Carlos", "Pedro", "Beatriz", "Maria"]
sorteio_estudante = random.randint(0, len(participantes) - 1)
lider = participantes[sorteio_estudante]


print(f"O estudante lider e : {lider}")
