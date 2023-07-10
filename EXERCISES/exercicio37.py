# numero converter para 
# binario
# octal
# hexadexcimal

#import bin

num = int (input ('Digite um número: '))

#escolha = int (input ('Escolha uma das bases para conversão: vc deseja: [1] para binário  [2]para octal e  [3] para hexagonal: '))
print ('''Escolha uma das bases para conversão: 
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
opcao = int (input ('Sua opção: '))


if opcao ==  1 :
    #  convertToBinary(num//2)
    #  print(num % 2,end = '')
    binary = bin(num)[2:]
    print ('O valor convertido {} em binário é: {}' .format(num, binary))

elif opcao == 2:
    octal = oct(num)[2:]
    print ('O valor {} convertido em octal é: {}' .format(num, octal))
elif opcao == 3:
    hexa = hex(num)[2:]
    print ('O valor {} convertido em hexadecimal é: {}' .format(num, hexa))
else:
    print ('Opção {} invalida, escolha 1, 2 ou 3:')
    
# print ('O valor convertido é: ')
