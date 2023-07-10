# Faça um programa pergunte um número ao jogador e tembém se ele escolhe par ou ímpar, 
# o computador vai jogar um número e a soma desse numero vai dizer se o jogador ou não que ganhou 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 


from random import randint


"""
itens = ('Pedra' , 'Papel' , 'Tesoura')
# escolhido = random.choice(lista)
#computador = choice(lista)
computador = randint(1, 2)

print ('Você escolheu {} ' .format (itens [jogador] ))
"""


vitorias = 0
#print ('Você escolheu {} ' .format (itens [jogador] ))
computador = 0
jogador = -1
#while computador != jogador :
soma = 0
resultadoparimpar = 0
while True :
    computador = randint(0, 10)
    computadorparimpar = randint(0, 1)
    
    itens = ('impar' , 'par')

    jogadornum = int (input ('Digite um número: '))
    
    jogadorpi =  ' '
    while jogadorpi not in 'PI' :
        jogadorpi = str (input ('Par ou Impar [ P/I]: ')).strip().upper()[0]

    if jogadorpi == 'P' :
        jogadorpi = 'par'
    elif jogadorpi == 'I': 
        jogadorpi = 'impar'

    #print ('jogadorpi {} ' .format ( itens [jogadorpi] ))

    soma = computador + jogadornum
    if soma % 2 == 0 :
        resultadoparimpar = 'par'
    else :
        resultadoparimpar = 'impar'

    print ('Voce escolheu {} o computador escolheu {} o total é {} deu {} ' .format (jogadornum, computador, soma, resultadoparimpar ))
    
    print (f'jogadorpi {jogadorpi} e resultadoparimpar {resultadoparimpar}')
    if jogadorpi == resultadoparimpar : 
        print ('-=' *15)
        print ('     Você Ganhou!     ')
        print ('-=' *15)
        vitorias += 1

    else :
        print ('-=' *15)
        print ('     Você Perdeu!     ')
        print ('-=' *15)
        break

print ('GAME OVER!', end = ' ')
if pontos == 1 :
    print (f'Você ganhou {vitorias} vez') 
elif  pontos != 1 : 
    print (f'Você ganhou {vitorias} vezes') 






