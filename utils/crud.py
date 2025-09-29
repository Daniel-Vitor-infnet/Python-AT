import os

DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_DIR = os.path.dirname(DIR)

ARQ = os.path.join(ROOT_DIR, "produtos.csv")


def ler_arquivo():
    produtos = []
    try:
        with open(ARQ, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                campos = linha.strip().split(",")
                id, produto, quantidade, preco = int(
                    campos[0]), campos[1], int(campos[2]), float(campos[3])
                produtos.append([id, produto, quantidade, preco])
    except Exception as ex:
        print(f"Erro ao ler o arquivo: {ex}")
    return produtos


# Sei que n existe "update" no csv, porém achei a propriado.
def atualizar_estoque_temporario(estoque, compra_feita):
    for produto in estoque:
        for item in compra_feita:
            if produto[0] == item[0]:
                produto[2] -= item[1]

    return estoque


def atualizar_estoque(produtos):
    try:
        with open(ARQ, "w", encoding="utf-8-sig") as arquivo:
            for produto in produtos:
                linha = f"{produto[0]},{produto[1]},{produto[2]},{produto[3]}\n"
                arquivo.write(linha)
    except Exception as ex:
        print(f"Erro ao salvar o arquivo: {ex}")
