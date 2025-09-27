import utils.crud as crud
import utils.tools as tools

estoque = crud.ler_arquivo()
cliente_num = 0

tools.exibir_estoque(estoque)

print("""
[1] - Cadastrar Produto
[2] - Listar Produtos
[3] - Atualizar Produto
[4] - Deletar Produto
[0] - Sair
""")