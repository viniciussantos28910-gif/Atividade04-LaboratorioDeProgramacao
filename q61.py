lst = ["python2023", "0203programacao2023", "luz azul",
       "arara rara", "anotaram a data da maratona"]


def str_invert(lista):
    resultado = []

    for texto in lista:

        if " " in texto:
            palavras = texto.split()
            palavras_invertidas = []

            for p in palavras:
                palavras_invertidas.append(p[::-1])

            frase_final = " ".join(palavras_invertidas[::-1])
            resultado.append(frase_final)

        else:

            resultado.append(texto[::-1])

    for i, e in enumerate(resultado):
        print(f"{i+1}. {e}")


str_invert(lst)
