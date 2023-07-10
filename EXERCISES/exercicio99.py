# Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maiorDef (num, maior):
    if num > maior :
        maior = num
 
def maior3 ( * num2) :
    cont2 = 0
    maior3 = 0
    print ('-=' * 22)
    print (f'Analisando os valores passados ....')
    for valor in num2 :
        print (f'{valor} ', end = '')
        sleep (0.3)
        #print (maior3)
        if cont2 == 0 :
            maior3 = valor
        else: 
            if valor > maior3 :
                maior3 = valor
        cont2 += 1
    print (f'\nForam informados: {cont2}')
    print (f'O maior valor informado foi: {maior3}')
    print ('-=' * 22)
     
     
        

from time import sleep
numeros = list ()
maior = 0
num = 0
cont = 0
c = 1



#numeros.append(0)
while True :
    #num = int (input ('Digite um número: '))
    
    while True:
        try:
            num = int (input ('Digite um número: '))
            break
        except:
            print("Número inválido")
        #if num == 999 :
        #    break
        
    #maiorDef (num, maior)
    #print (maior)
    #print (maior2)


    #"""
    if num > maior :
        maior = num
        c += 1
        #print (f'C {c}')
    #"""
    
    numeros.append(int(num)) 
    
    cont += 1
    
    print (f'COUNT {cont}')
    print (f'Maior {maior}')
    print (f'numeros {numeros}')
    
    while True : 
        resp = str (input ('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN' :
            break
        else: # resp != 'SN' :
            print ('ERRO! Digite S ou N')

    if resp == 'N' :
        break



maior3 (2,5,7,1,9,0,3,22,1)




#print (f'C {c}')
#print (f'COUNT {cont}')
#print (f'Maior {maior}')
print (f'numeros informados {numeros}')

print (f'Analisando os números passados...')
sleep(0.5)
print (f'Foram informados {cont} valores.')
print (f'O maior número é: {maior}.')
print ('FIM!')






