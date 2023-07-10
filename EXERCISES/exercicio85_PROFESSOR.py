#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


num = [[],[]]
entrada = 0
for c in range (1, 8) :
    entrada = int (input (f'Digite um {c} valor: '))

    #num.append (entrada)
    #print (num)
    
    #for c in range (0, len(num)) :
    if entrada % 2 == 0 :
        num[0].append (entrada)
        #print (par)
    else: 
        num[1].append (entrada)
        #print (impar)


print (f'A lista de números digitada: {num}')
num[0].sort ()
num[1].sort ()
print (f'Os números pares: {num[0]}')
print (f'Os números impares: {num[1]}')
print (f'Os números pares e impares em ordem crescente: {num}')


