def disount_calc(lst: list[str]):

    try:
        for i in lst:
            float(i)
    except ValueError as erro:
        print(f"ERRO: {erro}")
    else:
        lst = [float(i)*0.9 for i in lst]
        return lst

lst = ["23.99", "56.99", "103.99", "0.99"]
for i in disount_calc(lst):
    print(f"{i:.2f}")