from Placar import Placar
# Jogos trabalham dentro de um loop infinito
# se colocasse 6==5 nunca ia ser verdadeiro
# se colocasse 6!==5 nunca ia ser verdadeiro
# um print dentro de um loop infinito é o que atrasa, é um comando complexo, até achar uma saída padrão
# for joao in range(1000):
    #print (f"({joao}) oi")
# com and 99 condições verdadeiras e uma falsa, o resultado é falso
# COM OR 99 CONDIÇÕES FALSAS E UMA UNICA VERDADEIRA O RESULTADO É VERRDADEIRO

#IMPORTAR MÓDULO EXTERNO
import random as rd

#variáveis que determinam a vida inicial
vidaJogador = 5
vidaInimigo = 5 #notação do camelo (camel case)

qtdAtaque = 3 

#criando itens de um inventário com uma lista, usa-se chaves para lista
itens = ["espada","cura","armadura"]
#agora gerar esses itens aleatoriamente, toda lista cria um indice
#indice => [0   ,1    ,2     ] ou seja, indice = [espada, cura, armadura]
# se chamar: print(itens[1]) o resultado será cura
iventario=[] 

while vidaJogador>0 and vidaInimigo>0:
        # Placar
        Placar(vidaJogador, vidaInimigo, qtdAtaque)
        potencia = rd.randint(0,3)
        
        #para aparecer um intem de forma aleatoria dos que aparecem na lista, ordenamos de zero ao numero da casa 
        # ex: item = rd.randint(0,2)
        
        #caso você queira aumentar a quantidade de itens da lista vai precisar trocar o ultimo número do randint
        #A menos que vc use a função 'len' que da o numero total de casa da lista ou de caracteres de uma string
        #ou seja como para randomizar a contagem começa de zero escrevemos 'len(itens)-1'
        item = rd.randint(0,len(itens)-1)
        
        print(f"Dropando: {itens[item]}")
        
        x = input(f"armazenar item {itens[item]} S/N?").upper()
        if x =='S':
            iventario.append(itens[item]) 
        
        if qtdAtaque>0:
            acao = input("[A]taque ou [D]efesa? ").upper()        
        
        # Ação de Ataque do Jogador!
        if (acao == 'A') and (qtdAtaque>0):
            print("Jogador ataca!")
            print(f"Jogador atacou com força {potencia}!")
            #Subtraindo a qt de vida do inimigo (potencia)
            vidaInimigo -= potencia
            qtdAtaque -= 1
        # Ação de Defesa do Jogador
        else:
            # variável = Verdadeiro IF (condição) ELSE Falso
            potDefesa = rd.randint(-2, 3) if (qtdAtaque>0) else rd.randint(-3, -1)
            print("Jogador Defende!")
            print(f"Jogador usou defesa: {potDefesa}!")
            vidaJogador  = potDefesa
        
        # pausa
        pausa = input('Pressione uma tecla pra continuar')
if vidaJogador<=0:
    print("Inimigo venceu!")
elif vidaInimigo<=0:
    print("Jogador venceu!")
else :
    print("Game over!!!")



