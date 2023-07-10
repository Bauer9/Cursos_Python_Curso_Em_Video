#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


num = int ( input ('Digite um número: '))
cont = 0

for c in range (1, num + 1) :
    if num % c == 0 :
        print ('\33[33m', end = '')
        cont += 1
    else :
        print('\33[31m', end = '')
    


    print ('{} ' .format(c), end = '')

print ('\n\33[mO número {} foi divisível {} vezes' .format(num, cont)

if cont == 2 :
    print ('\nE por isso ele é \33[32mPRIMO!')
else : 
    print ('\n\33[mOE por isso ele \33[31mNÃO \33[mé \33[31mPRIMO')






"""
#    if num // 2 and num // 3 and num // 5 and num // 5 and num //7 :
    num = num / 2
    cont = cont + 1
       if count = 

#       if num % 1 == 0 and num % num == 0 :
#            cont = cont + 1
#            if cont == 2 :
#                print ('O número {} é divisivel {} vezes' .format (num, loop))
#                print ('E po isso ele é PRIMO!')
    print ('{:.2f}' .format(num))




print ('2, 3, 5, 7, ', end = '')
for p in range (1, 101) :
#    print ('{}' .format(p), end = ', ') 

    if p > 2 and p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0 :
            print ('{}' .format(p), end = ', ') 
print ('FIM !')
"""


