"""
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes

"""

print ( '-='*20 )
print ('Analisador de triangulos versão 2')
print ( '-='*20 )

a = float (input( 'Digite o primeiro segmento: ' ))
b = float (input( 'Digite o segundo segmento: ' ))
c = float (input( 'Digite o terceiro segmento: ' ))

if a < b+c and b < a + c and c < a + b:
    print ('SIM!. Os segmentos acima formam um triângulo!')
    if a == b == c :
        print ('EQUILÁTERO')
    elif a == b or b == c or c == a :
        print ('ISÓSCELES')   
    else:
        print ('ESCALENO')

else:
    print ('NÃO. Os segmentos acima não formam um triangulo')
    triangulo = 'nao'


triangulo == 'sim'



