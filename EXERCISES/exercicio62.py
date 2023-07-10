# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

"""
    if contador >= 10 :
        print ('PAUSE!')
        maistermos = int (input ('Quantos termos a mais vc quer? '))
        print ('{}' .format (termo), end = ' - ' )
        #contador = contador + 1
        termo += razao
        contador == 0
"""

"""
if contador == maistermos :
    print ('PAUSE!')
    maistermos = int (input ('Quantos termos a mais vc quer? '))
    contador2 == 0
else maistermos == 0 :
"""

print ( '=' * 38 )
print ( '  Progressão Aritmética v3 com WHILE  ' )
print ( '=' * 38 )

primeiro = int (input ('Digite o Primeiro Termo: '))
razao = int (input ('Razão: '))


contador = 1
termo = primeiro
total = 0
mais = 10
while mais != 0 :
    total = total + mais
    while contador <= total :
        print ('{}' .format (termo), end = ' - ' )
        termo += razao
        contador = contador + 1

    print ('PAUSA!')
    mais = int (input ('Quantos termos a mais vc quer? '))


print ('FIM1')
print ('Progressão finalizada com {} termos' .format(total))
