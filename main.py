import utils.crud as crud
import utils.tools as tools
from tabulate import tabulate
from datetime import datetime


estoque = crud.ler_arquivo()
cliente_num = 0
expediente_fechado = []

print("====== ATENDIMENTO INICIADO ======")

while True:
    cliente_num += 1

    itens_comprados = tools.confirmar_compra(estoque)
    clientes_totais = tools.gerar_nota_fiscal(cliente_num, estoque, itens_comprados)
    estoque = crud.atualizar_estoque_temporario(estoque, itens_comprados)


    if tools.verificar_escolha("Deseja atender o próximo cliente?") == "s":
        continue
    else:
        expediente_fechado.append(clientes_totais)
        crud.atualizar_estoque(estoque)
        
        print("====== ATENDIMENTO FINALIZADO ======")
        # A data n lembrava peguei da net memu
        print(datetime.now().strftime("%d/%m/%Y %H:%M\n"))

        print(tabulate(expediente_fechado, headers=["Cliente", "Total"], tablefmt="fancy_grid"))
        tools.calcular_total_vendas(expediente_fechado)

        tools.produtos_sem_estoque(estoque)

        break
