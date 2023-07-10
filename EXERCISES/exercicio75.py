"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
#
"""
c = 0
while c < 4 :
    num = (int (input ('Digite um número:')))
    print (num)
    
    print (num+c)
    c+= 1
    tupla_vazia = () # Também é possível fazer: tupla_vazia = tuple()
    print("Tupla vazia: ", tupla_vazia)


    if c == 4 :
        lista = (num) 
        print (lista)

"""

#PROFESSOR
num =  (int (input ('Digite um número:')),
        int (input ('Digite um número:')),
        int (input ('Digite um número:')),
        int (input ('Digite um número:')))

print (f'Voc6e digitou os valores {num}')   

if 9 in num :
    print (f'O 9 apareceu: {num.count (9)+1} vezes')
else :
    print ('O valor 9 não foi digitado')

if 3 in num :
    print (f'O primeiro 3 está na: {num.index (3)+1} posição')
else :
    print ('O valor 3 não foi digitado')


print ('Os valores pares digitados são: ', end ='')
for n in num :  
    if n % 2 == 0 :
        print (n, end = ' ')
   
print ('\nFIM')