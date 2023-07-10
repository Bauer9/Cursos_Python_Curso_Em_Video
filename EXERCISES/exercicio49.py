# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.



print ( '=' * 11 )

print ('  TABUADA')

print ( '=' * 11 )



num = int (input ('Digite qual tabuada voc6e deseja ver: '))

for t in range (1, 11):
    print ('{} x {:2} = {:2}' .format (num, t, num * t))



