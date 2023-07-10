#
# Programa que leia um numero inteiro e diz se é par ou impar



num = int (input ('Digite um número inteiro e veja se ele é par ou impar: '))

"""
if (re % 2) == 0:
    print ('O número {} é par:' .format(num))
else:
    print ('O número {}, é impar'.format(num))

"""

"""

if num % 2:
    print ('O número {} é impar:' .format(num))
else:
    print ('O número {}, é par'.format(num))
"""

resultado = num % 2
if resultado == 0:
    print ('O número {} é par:' .format(num))
else:
    print ('O número {}, é impar'.format(num))

