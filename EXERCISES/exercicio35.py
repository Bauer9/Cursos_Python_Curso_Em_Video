#(
# leia o comprimento de 3 retas e diga se pode ou não formar um triângulo
# 
# 
# 
# Dica: r1 e r2 precisam ser maiores que r3
#  
# )


print ( '-='*20 )
print ('Analisador de triangulos')
print ( '-='*20 )

a = float (input( 'Digite o primeiro segmento: ' ))
b = float (input( 'Digite o segundo segmento: ' ))
c = float (input( 'Digite o terceiro segmento: ' ))


"""
#CONDIÇÃO: a soma de dois lados é sempre menor que o terceiro lado.
if a+b > c and a+c > b and b+c > a:
    print ('SIM!. Os segmentos acima formam um triângulo!')
else:
    print ('NÃO. Os segmentos acima não formam um triangulo')
"""


if a < b+c and b < a + c and c < a + b:
    print ('SIM!. Os segmentos acima formam um triângulo!')
else:
    print ('NÃO. Os segmentos acima não formam um triangulo')



