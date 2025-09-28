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
    
    expediente_fechado.append(clientes_totais)


    if tools.verificar_escolha("Deseja atender o próximo cliente?") == "s":
        estoque = crud.update_arquivo(estoque, itens_comprados)
        continue
    else:
        
        print("====== ATENDIMENTO FINALIZADO ======")
        print(datetime.now().strftime("%d/%m/%Y %H:%M")) # A data n lembrava peguei da net memu
        
        print(tabulate(expediente_fechado, headers=["Cliente", "Total"], tablefmt="fancy_grid"))
        tools.calcular_total_vendas(expediente_fechado)
        break
