# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.



from random import randint

acertou = False
computador = randint (0, 10)
palpites = 0
jogador = 0
while not acertou :
    jogador = int (input ('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador :
        acertou = True
    else:
        if jogador < computador :
            print ('É maior, tente mais uma vez')
        elif jogador> computador :
            print ('É menor, tente novamente')
print ('Acertou!')
print ('Você fex {} tentativas' .format (palpites))







