from tabulate import tabulate
from datetime import datetime

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

def verificar_id_duplicado(produtos_comprados, produto_id): # Eu ia fazer uma função pra atualizar a quantidade, mas me enbananei e desisti por causa do tempo.
    for item in produtos_comprados:
        if item[0] == produto_id:
            return True
    return False


def verificar_escolha(msg):
    while True:
        escolha = input(f"{msg} (s/n): ").lower()
        if escolha in ["s", "n"]:
            return escolha
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")


def verificar_estoque(estoque, produto_id, qtd):
    for produto in estoque:
        if produto[0] == produto_id:
            return bool(produto[2] >= qtd)
                 
            
def confirmar_compra(estoque):
    produtos_comprados = []
    while True:
        
        id_produto = verificar_id()
        
        if verificar_id_duplicado(produtos_comprados, id_produto): # Eu ia fazer uma função pra atualizar a quantidade, mas me enbananei e desisti por causa do tempo.
            print("Produto já adicionado. Escolha outro produto.")
            if verificar_escolha("Deseja verificar o estoque?") == "s":
                exibir_estoque(estoque)
            continue
        
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
        
        
def gerar_nota_fiscal(cliente_num, estoque, produtos_comprados):
    total = 0
    lista_produtos = []
    
    for item in produtos_comprados:
        id_produto = item[0]
        qtd = item[1]
        for produto in estoque:
            if produto[0] == id_produto:
                preco = produto[3]
                subtotal = preco * qtd
                total += subtotal
                lista_produtos.append((id_produto, produto[1], qtd, preco, subtotal))

    print("====== NOTA FISCAL ======\n")
    print(f"Cliente número: {cliente_num}")
    print(datetime.now().strftime("%d/%m/%Y %H:%M")) # A data n lembrava peguei da net memu
    print(tabulate(lista_produtos, headers=["ID", "Produto", "Quantidade", "Preço Unitário", "Subtotal"], tablefmt="fancy_grid"))
    print(f"\nQuantidade de Itens: {len(produtos_comprados)}")
    print(f"Total: R$ {total:.2f}")

    return [f"Cliente : {cliente_num}", total]


def calcular_total_vendas(vendas):
    total_vendas = 0
    for cliente in vendas:
        total_vendas += cliente[1]
    
    return print(f"Total de Vendas do Dia: R$ {total_vendas:.2f}")


def produtos_sem_estoque(estoque):
    sem_estoque = []
    for produto in estoque:
        if produto[2] == 0:
            sem_estoque.append(produto)

    print("\nProdutos sem estoque:")
    print(tabulate(sem_estoque, headers=["ID", "Nome", "Quantidade", "Preço"], tablefmt="fancy_grid"))
    return 
