import utils.crud as crud
import utils.tools as tools

estoque = crud.ler_arquivo()
cliente_num = 0

# tools.exibir_estoque(estoque)

print("====== ATENDIMENTO INICIADO ======")

  while True:
      cliente_num += 1
      
      itens_comprados = tools.confirmar_compra(estoque)
      tools.gerar_nota_fiscal(cliente_num, estoque, itens_comprados)
      
      if tools.verificar_escolha("Deseja atender o próximo cliente?") == "s":
          continue
        else:
            print("====== ATENDIMENTO FINALIZADO ======")
            break






