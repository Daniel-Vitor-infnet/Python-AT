import utils.crud as crud
import utils.tools as tools

estoque = crud.ler_arquivo()
cliente_num = 0

# tools.exibir_estoque(estoque)

print("====== ATENDIMENTO INICIADO ======")

#  while True:
#      cliente_num += 1
#      print(f"Cliente número: {cliente_num}")
     
     
print(tools.confirmar_compra(estoque))
         



