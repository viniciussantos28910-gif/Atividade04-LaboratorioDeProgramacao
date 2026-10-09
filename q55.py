disciplinas = ("Matematica", "Portugues")
registro_escola = {}

while True:

    nome = input("Nome do estudante (ou pressione ENTER pra sair): ")
    if not nome:
        break
    mat = float(input("Nota de Matematica: "))
    port = float(input("Nota de Portugues: "))
    media = (mat+port) / 2
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    registro_escola[nome] = {
        "Matematica": mat,
        "Portugues": port,
        "Media": media,
        "Situacao": situacao
    }

print("Disciplinas escolares: {disciplinas}")
print("\n Relatorio do registro escolar:")
for aluno, dados in registro_escola.items():
    print(
        f"Aluno: {aluno}, Media: {dados['Media']:.2f} , Situacao: {dados['Situacao']}")
