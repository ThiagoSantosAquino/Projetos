""" exmplo em que for não serve

for menu in range(10):
 print('*'*30)
 print("\t\tcontrole de estoque")
 print("1 - /incluir o Produto")
 print("2- Alterar preço")
 print("3 - Excluir produto")
 print('*'*30)
 print(" S para sair do controle de estoque")
 opcao:str = input("==> ")
 if opcao=='1':
    print("Você escolheu inclur")
 elif opcao=='2':
    print("você escolheu Alterar o preço")
 elif opcao=='3':
    print("você escoheu Exclui o produto")
 else:
     print("Nenhma opção foi escolhida")"""

# agora usaremos a função while

from alteracao import alterar
from exclusao import excluir
from inclusao import incluir

opcao='0' 
while opcao != 'S':
 print('*'*30)
 print("\t\tcontrole de estoque")
 print("1 - /incluir o Produto")
 print("2- Alterar preço")
 print("3 - Excluir produto")
 print("S para sair do controle de estoque")
 print('*'*30)
 
 opcao:str = input("==> ")
 if opcao=='1':
    print("Você escolheu incluir")
    incluir()
 elif opcao=='2':
    alterar
 elif opcao=='3':
    excluir
 elif opcao=='S':
    print("Você escolheu sair")
 else:
    print("opção inválida")