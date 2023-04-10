from inclusao import *
from menualteracao import *
from exclusao import *
from relatorios import *

def menu():
    print("="*50)
    print("1- Inclusão de produto")
    print("2- Alteração de dados")
    print("3- Exclusão de produto")
    print("4- Relatório")
    print("="*50)
    
    opcao = input('').upper()
    #Cria-se um dicionário a seguir para associar com a resposta do usuário
    opcoesMenu = {
        '1': "inclusao()",
        '2': "menuAlterar()",
        '3': "excluir()",
        '4': "relatorios()",
        '5': "exit()"
    }

    eval(opcoesMenu[opcao])
# End menu()2
menu()
    
    