from tabulate import tabulate

def exibir_estoque(estoque):
    print("====== ESTOQUE DE PRODUTOS ======")
    print(tabulate(estoque, headers=["ID", "Nome", "Quantidade", "Preço"], tablefmt="fancy_grid"))

def verificar_id(id):
    while True:
        if id >= 1 and id <= 5:
            return id
        else:
            id = int(input("ID inválido. Digite um ID do produto entre 1 e 5: "))

def verificar_estoque(estoque, produto_id, qtd):
    for produto in estoque:
      
        if produto[0] == produto_id:
            produto[2] -= qtd
            return True
    return False

def confirmar_compra(estoque):
    while True:
        id_produto = verificar_id()
        
        qtd = int(input("Digite a quantidade do produto: "))
        
        qtd_produto = verificar_estoque(estoque, id_produto, qtd)
        
        if not qtd_produto:
            print("Quantidade indisponível no estoque. Abaixo vou enviar o estoque atualizado para fazer a escolha correta.")
            exibir_estoque(estoque)
            continue
        else:
            return [id_produto, qtd]
        
        
        
    