from tabulate import tabulate

def exibir_estoque(estoque):
    print("====== ESTOQUE DE PRODUTOS ======")
    print(tabulate(estoque, headers=["ID", "Nome", "Quantidade", "Preço"], tablefmt="fancy_grid"))
