def incluir():
    LisProd = []
    
    print('-'*30)
    print(" Você optou por incluir o produto:")
    codigo:int(input("Digite o código do produto:"))
    descrt:str(input("descreva a carctaristica do produto:"))
    preco:float(input("Digite o valor do preço:"))
    quant:float(input("digite a quantidade incluída"))
    
    LisProd.append([codigo,descrt,preco,quant])