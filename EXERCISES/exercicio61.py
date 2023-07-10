# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
\

print ( '=' * 38 )
print ( '  Progressão Aritmética V2 com WHILE  ' )
print ( '=' * 38 )

primeiro = int (input ('Digite o Primeiro Termo: '))
razao = int (input ('Razão: '))
decimo = primeiro + (10 - 1) * razao

"""
for c in range ( primeiro, decimo + razao, razao ) :
    print ('{}' .format (c), end = ' - ' )



contador = primeiro # MINHA SOLUCAO 1
while contador < decimo + razao :

    print ('{}' .format (contador), end = ' - ' )
    contador = contador + razao

print ('ACABOU!')


""" 
# SOLUCAO PROFESSOR SEM USAR O DECIMO 
contador = 1
termo = primeiro
while contador <= 10 :

    print ('{}' .format (termo), end = ' - ' )
    contador = contador + 1
    termo += razao

print ('ACABOU!')

