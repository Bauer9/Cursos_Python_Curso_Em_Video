# faça um programa que leia um número de 0 a 9999 e mostre na tela cada dígito separado 
# ex: digita 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1



"""
num = (input('Digite um número: '))

print ('O número de unidade é {}' .format (num[0]))
print ('O número de desena é {}' .format (num[1]))
print ('O número de centena é {}' .format (num[2]))
print ('O número de milhar é {}' .format (num[3]))

"""

num = int (input('Digite um número: '))

u = num //1 % 10
d = num //10 % 10
c = num //100 % 10
m = num //1000 % 10

print ('Analisando o número {}'.format(num))
print ('unidade: {}'.format(u))
print ('dezena: {}'.format(d))
print ('centena: {}'.format(c))
print ('milhar: {}'.format(m))
