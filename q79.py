import traceback

estoque = {}

def cadastrar_produto(nome, preco, quantidade):
    try:
        if len(nome) <= 0:
            raise ValueError("O campo e nao pode estar vazio")
        elif float(preco) <= 0:
            raise ValueError("O produto nao e de graca")
        elif int(quantidade) < 0:
            raise ValueError("Nao pode  ter uma quantidade negativa de itens")

    except (ValueError, TypeError) as erro:
        print(erro)
        traceback.print_exc()
        return cadastrar_produto(input("Nome do produto: "), input("Preco do produto: "), input("Quantidade do produto: "))

    else:
        estoque[nome] = {
            "preco": preco,
            "quantidade": quantidade
        }

    for k, v in estoque.items():
        print(f"{k}:")
        for t, c in v.items():
            print(f"\t{t}--{c}")

cadastrar_produto("jangada", "75", "89")