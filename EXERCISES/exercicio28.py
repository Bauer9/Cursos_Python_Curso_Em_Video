# 
# faça o computador pensar em um número inteiro de 1 a 5, e o usuário tenta advinhar o número e ele escreve na tela se o usuário ganhou ou perdeu

# num = random.randint(1, 10)


#import random
from random import randint
#random = random.randint(0,5)
random = randint(0,5) # faz o computador escolher um número entre 0 e 5
from time import sleep # fazer que está levando um tempo para mostrar a informação


print('Pensei em um númeto entre 0 e 5')
num = int (input (' Adivinhe o número que escolhi? '))
print('PROCESSANDO...')
sleep(2)


if random == num:
    print ('Você ganhou!')
else:
    print ('Você perdeu!, o número é {}' .format(random))
    print ('Tente novamente! :(')





