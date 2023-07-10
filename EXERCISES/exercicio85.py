#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num2 = list ()
num = list () # ou  mum = []
par = list ()
impar = list ()
entrada = 0
for c in range (0, 7) :
    entrada = int (input('Digite um valor: '))

    num.append (entrada)
    #print (num)
    
    #for c in range (0, len(num)) :
    if entrada % 2 == 0 :
        par.append (entrada)
        #print (par)
    if entrada % 2 != 0 :
        impar.append (entrada)
        #print (impar)


print (f'Par: {par}')
print (f'Impar: {impar}')
print (f'Num: {num}')
#print (f'Num2: {num2}')
num2 =  par[:] + impar [:]  
print (f'NUm2 crescente pares e impares: {num2}')
par.sort()
impar.sort()
num2 =  par[:] + impar [:]  
print (f'NUm2 crescente pares e impares Crescente: {num2}')

