ARQ = "C:/Users/NoobSupremo/Desktop/Backup (Pc)/Faculdade/Python/Programação com Python [25E3_2] (1º trimestre)/Projetos/Python-AT/produtos.csv"

def ler_arquivo():
    produtos = []
    try:
        with open(ARQ, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                campos = linha.split(",")
                
                id = int(campos[0]) 
                produto = campos[1] 
                quantidade = int(campos[2])
                preco = float(campos[3])
                
                produtos.append([id, produto, quantidade, preco])
    except Exception as ex:
                print(f"Erro ao ler o arquivo: {ex}")
    return produtos

print(ler_arquivo())