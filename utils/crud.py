ARQ = "C:/Users/NoobSupremo/Desktop/Backup (Pc)/Faculdade/Python/Programação com Python [25E3_2] (1º trimestre)/Projetos/Python-AT/produtos.csv"

def ler_arquivo():
    produtos = []
    try:
        with open(ARQ, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                campos = linha.strip().split(",")
                
                id, produto, quantidade, preco = int(campos[0]), campos[1], int(campos[2]), float(campos[3])
                
                produtos.append([id, produto, quantidade, preco])
    except Exception as ex:
        print(f"Erro ao ler o arquivo: {ex}")
    return produtos


def salvar_arquivo(produtos):
    try:
        with open(ARQ, "w", encoding="utf-8") as arquivo:
            for produto in produtos:
                linha = f"{produto[0]},{produto[1]},{produto[2]},{produto[3]}\n"
                arquivo.write(linha)
    except Exception as ex:
        print(f"Erro ao salvar o arquivo: {ex}")