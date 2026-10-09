from datetime import datetime
from pathlib import Path

pasta_atual = Path(__file__).parent
ARQUIVO_VENDAS = pasta_atual / "vendas.txt"
ARQUIVO_LOG = pasta_atual / "log_erros.txt"
BORDA = "=" * 46


class NomeVazioError(Exception):
    pass


class PrecoInvalidoError(Exception):
    pass


class QtdInvalidaError(Exception):
    pass


def validar_venda(nome, valor, qtd):
    if not nome.strip():
        raise NomeVazioError("O nome do produto não pode ser vazio.")

    try:
        valor = float(valor.replace(",", "."))
    except ValueError:
        raise PrecoInvalidoError("O preço deve ser um número.")
    if valor <= 0:
        raise PrecoInvalidoError("O preço deve ser maior que zero.")

    try:
        qtd = int(qtd)
    except ValueError:
        raise QtdInvalidaError("A quantidade deve ser um número inteiro.")
    if qtd <= 0:
        raise QtdInvalidaError("A quantidade deve ser um inteiro positivo.")

    return {"produto": nome.strip(), "preco": valor, "quantidade": qtd, "total": valor * qtd}


def salvar_texto(caminho, linha_texto):
    try:
        with open(caminho, "a", encoding="utf-8") as arq:
            arq.write(linha_texto + "\n")
    except OSError as e:
        print(f"  Não foi possível gravar em {caminho.name}: {e}")


def mostrar_relatorio(lista):
    print(f"\n{BORDA}\n{'RELATÓRIO DE VENDAS':^46}\n{BORDA}")

    if not lista:
        print("  Você ainda não registrou nenhuma venda.")
        print("  Volte ao menu e escolha a opção 1 para começar.")
        return

    print(f"{'Produto':<22}{'Qtd':>5}{'Preço':>9}{'Total':>10}")
    contagem = {}
    for venda in lista:
        print(
            f"{venda['produto']:<22}{venda['quantidade']:>5}{venda['preco']:>9.2f}{venda['total']:>10.2f}")
        contagem[venda["produto"]] = contagem.get(
            venda["produto"], 0) + venda["quantidade"]

    total_geral = sum(venda["total"] for venda in lista)
    campeao = max(contagem, key=contagem.get)

    print("-" * 46)
    print(f"Total de vendas.....: {len(lista)}")
    print(f"Produto mais vendido: {campeao} ({contagem[campeao]} un.)")
    print(f"Faturamento total...: R$ {total_geral:.2f}")
    print(f"Ticket médio........: R$ {total_geral / len(lista):.2f}")


def cadastrar_venda(lista):
    nome = input("\n  Por favor, informe o nome do produto: ")
    if nome.strip().lower() == "fim":
        return False
    valor = input("  Informe o preço unitário (R$): ")
    qtd = input("  Informe a quantidade vendida: ")

    while True:
        try:
            dados = validar_venda(nome, valor, qtd)
        except (NomeVazioError, PrecoInvalidoError, QtdInvalidaError) as e:
            print(f"  [ERRO] {e} Vamos corrigir?")
            salvar_texto(
                ARQUIVO_LOG, f"{datetime.now():%d/%m/%Y %H:%M:%S} - {type(e).__name__}: {e}")

            correcao = input(
                "  Digite o valor correto (ou 'cancelar' para desistir): ")
            if correcao.strip().lower() == "cancelar":
                print("  Tudo bem, a venda foi cancelada. Nada foi gravado.")
                break
            if isinstance(e, NomeVazioError):
                nome = correcao
            elif isinstance(e, PrecoInvalidoError):
                valor = correcao
            else:
                qtd = correcao
        else:
            lista.append(dados)
            salvar_texto(
                ARQUIVO_VENDAS, f"{dados['produto']};{dados['preco']:.2f};{dados['quantidade']};{dados['total']:.2f}")
            print(
                f"  [OK] Venda registrada com sucesso! Total: R$ {dados['total']:.2f}")
            break
        finally:
            print("  " + "-" * 30)
    return True


lista_vendas = []

print(f"\n{BORDA}\n{'Bem-vindo(a) à LOJA VIRTUAL!':^46}\n{BORDA}")
print("  Para começar, escolha a opção 1 e cadastre uma venda.")

try:
    while True:
        print(f"\n{BORDA}\n{'MENU PRINCIPAL':^46}\n{BORDA}")
        print(f"  [1] Registrar venda   (vendas hoje: {len(lista_vendas)})")
        print("  [2] Ver relatório\n  [3] Encerrar")
        op = input("\n  Escolha uma opção: ").strip().lower()

        if op == "1":
            if not cadastrar_venda(lista_vendas):
                break
        elif op == "2":
            mostrar_relatorio(lista_vendas)
        elif op in ("3", "fim"):
            break
        else:
            print("  Opção inválida. Por favor, escolha 1, 2 ou 3.")
except (KeyboardInterrupt, EOFError):
    print("\n\n  Encerrando o programa a pedido do usuário...")

if lista_vendas:
    mostrar_relatorio(lista_vendas)
print("\n  Obrigado por usar o sistema. Até logo!")
