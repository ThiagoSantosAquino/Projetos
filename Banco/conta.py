from datatime import date

class Contas:
    #método construtor
    '''
    tipo 1 - CONTA CORRENTE
    TIPO 2 - CONTA POUPANÇA
    TIPO 3 - CONTA INVESTIMENTO
    '''
    
    def __init__(self, conta, agencia, cliente, tipo='1'):
        
        self.nAgencia = agencia
        self.nConta = conta
        self.ntipo = tipo
        self.correntista = cliente
        self._saldo = 0 # _ é uma convenção para identificar variáveis privadas
        self.data = date.today() 