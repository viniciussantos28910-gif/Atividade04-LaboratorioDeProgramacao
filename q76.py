import traceback


def pro_e(lst: list[str | int]) -> bool:
    try:
        for i, e in enumerate(lst):
            if i % 2 != 0:
                if not isinstance(e, int):
                    raise TypeError(
                        "Indice impar, mas o valor nao e 'integer'")
                elif e % 7 != 0:
                    raise ValueError("O valor nao e multiplo de 7")

            if i % 2 == 0:
                if not isinstance(e, str):
                    raise TypeError(
                        "O indice e par, mas o valor nao e 'string'")
                elif any(str(x) in e for x in range(10)):
                    raise ValueError("A string contem numeros")

    except (ValueError, TypeError) as erro:
        print(erro)
        traceback.print_exc()
        return False

    else:
        return True


lst_c = ["afr", 7, "aff", 14, "jhfd", 21]
lst_f = ["3rf", 7, 6, "fsd4", "gfh"]

print(pro_e(lst_c))
print(pro_e(lst_f))
