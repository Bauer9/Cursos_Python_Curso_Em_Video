"""
Exercício Python 048: Faça um programa que calcule a soma entre todos os números que 
# são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""


"""

if n % 3 == 0 :
    soma = n + n
    print ("A soma é {}" .format(soma))

    
    if c % 3 ==0 :
        print ( c )
"""


soma = 0 
contador = 0
contador1 = 0
for c in range (1, 501, 2) :
#    print ('.', end= "")  # Quantidade de LOOPS
#    print (c)
    if c % 3 ==0 :
        print ( c, ',', end = "" )
        contador1 = contador1 + 1  # contador1 = contador1 + 1 # contador1 += 1
        soma = soma + c # soma = soma + c # soma += c

    contador = contador + 1    # contador = contador + 1 # soma += 1

print (' ACABOU,', 'A soma é {}' .format(soma))
print ('Foram somados {} números impares divisíveis por 3' .format (contador1))
print ('Foram somados {} números divisíveis por 3' .format (contador))



"""
soma = 0
soma += c
print ("A soma é {}" .format(soma))
"""
