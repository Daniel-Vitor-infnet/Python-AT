from tabulate import tabulate

def exibir_estoque(estoque):
    print("====== ESTOQUE DE PRODUTOS ======")
    print(tabulate(estoque, headers=["ID", "Nome", "Quantidade", "Preço"], tablefmt="fancy_grid"))

def verificar_id():
    while True:
        id = int(input("Digite o ID do produto: "))
        if id >= 1 and id <= 5:
            return id
        else:
            print("ID inválido. Digite um ID do produto entre 1 e 5: ")


def verificar_escolha(msg):
    while True:
        escolha = input(f"{msg} (s/n): ").lower()
        if escolha in ["s", "n"]:
            return escolha
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")


def verificar_estoque(estoque, produto_id, qtd):
    #print(estoque)
    for produto in estoque:
      
        if produto[0] == produto_id:
            if produto[2] <= qtd:
                return True
            else:
                return False
            
            
def confirmar_compra(estoque):
    produtos_comprados = []
    while True:
        id_produto = verificar_id()
        
        qtd = int(input("Digite a quantidade do produto: "))
        
        qtd_produto = verificar_estoque(estoque, id_produto, qtd)
        
        if not qtd_produto:
            print("Quantidade indisponível no estoque.")
            if verificar_escolha("Deseja verificar o estoque?") == "s":
                exibir_estoque(estoque)
            continue
        else:
            produtos_comprados.append([id_produto, qtd])
        
        opcao = verificar_escolha("Deseja adicionar mais produtos?")
        if opcao == "s":
            continue
        else:
            return produtos_comprados
        
    