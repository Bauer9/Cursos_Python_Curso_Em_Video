# (
# leia 3 números e diz qual o menor e o maior
# 
# 
# )


num1 = int (input ( 'Digite o primeiro número: ' ))
num2 = int (input ( 'Digite o segundo número: ' ))
num3 = int (input ( 'Digite o terceiro número: ' ))


"""
if num1 < num2 or num1 < num3:
    print ('o menor número é {}' .format(num1))

if num2 > num3 or num2 > num3:
        print ('o maior número é {}' .format(num2))

if num3 > num1 or num3 > num2:
        print ('o maior número é {}' .format(num3))
       
"""
# verificando o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
    
# verificando o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print ('O menor valor digitado foi: {}' .format(menor))
print ('O maior valor digitado foi: {}' .format(maior))