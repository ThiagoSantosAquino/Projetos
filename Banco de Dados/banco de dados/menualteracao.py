from alteracao import *

def menuAlterar():
    print("="*50)
    print("1 - Alteração de Descrição")
    print("2 - Alteração de Preço")
    print("3 - Alteração de Quantidade")
    print("4 - Alteração de Peso")
    print("5 - Alteração de Vencimento")
    print("-"*50)
    print("S - Sair")

    opcao = input('').upper()

    match (opcao):
        case '1':
            alterarDesc()
        case '2':
            alterarPreco()
        case '3':
            alterarQt()
        case '4':
            alterarPeso()
        case '5':
            alterarVencto()
        case 'S':
            return