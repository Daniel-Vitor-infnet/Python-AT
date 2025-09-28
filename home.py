import utils.crud as crud
import utils.tools as tools

estoque = crud.ler_arquivo()
cliente_num = 0

# tools.exibir_estoque(estoque)

print("====== ATENDIMENTO INICIADO ======")

#  while True:
#      cliente_num += 1
#      print(f"Cliente número: {cliente_num}")
#      id_procuto = tools.verificar_id()
#      qtd_produto = tools.verificar_estoque()
     
tools.confirmar_compra(estoque)

