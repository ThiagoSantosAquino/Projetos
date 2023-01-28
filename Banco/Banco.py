#criar um programa simulando o banco usando biblioteca

print("'"*30)
print("1 - Dados do Cliete")
print("2 - Saque")
print("3 - Depósito")
print("4 - Saldo")
print("S - Sair")
print("'"*30)

opcao = input("")
#criar dicionário para evitar o uso repetitivo de if´s

dic={
    "1": "cadastro()",
    "2": "saque()",
    "3": "deposito()",
    "4": "saldo()",
    "5": "emprestimo()",
    "S": "sair()"      
}

eval(dic[opcao])#função que cham o dicionário

#Cadastro
def cadastro():
    conta = input ("Digite o número da Conta:")
    nome = input ("Digite seu nome completo:")
    agencia = ("Digite o número de sua agência:")
    
    return  nome, agencia, conta

#Depositar
def deposito():
    valor = input("Digite o valor a ser depositado:")
    cc.movimentar('d', valor)
    
#Sacar:
def saque():
    valor=input("Informe o valor a ser sacado:")
    cc.movimentar('s', valor)
    
dados = cadastro() #tupla é igual a lista mas não pode ser alterado
cc = Contas(conta=dados[2],ag = dados[1], cliente = dados[0])