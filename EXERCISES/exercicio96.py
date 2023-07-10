#Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area (larg, comp) :
    area = larg * comp
    print (f'A área do terreno de {larg}m por {comp}m é de {area:.1f} m2.')
    
    
"""
def soma2 (a,b) :
    print (f'A = {a} e B = {b}')
    s = a + b
    print (f'A soma A + B = {s}')
"""

#PROGRAMA PRINCIPAL
print ('controle de terrenos')
print ('-' * 30)
l = float (input ('Largura (m): '))
c = float (input ('Comprimento (m): '))   

area(l, c)



