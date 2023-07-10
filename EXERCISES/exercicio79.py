# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

#MINHA OPÇÃO
#lista = []

#PROFESSOR
numeros = list ()

#resultanteLista= []
#numeros = 
count = 0
#while True:
#c = 0
element = 0
while True :
    n = int (input ('Digite um valor: '))

    if n not in numeros :
        numeros.append (int(n))
        print ('Valor adicionado com sucesso...') 
        print (numeros)      
    else: 
        print ('Valor duplicado, não vou adicionar...')

    continuar = str (input ('Quer continuar? [S/N]: ')).strip().upper()

    if continuar == 'N' : 
        break
    elif continuar == "S" :
        print ()
    elif continuar != 'SN' :
        continuar = str (input ('Quer continuar? [S/N]: ')).strip().upper()


print ('=-' * 20)
#print (numeros)

numeros.sort()
#print ()
print (f'Você adicionou os valores: {numeros}' )
#print ()
print ('=-' * 20)

"""
    #lista.append (int (input ('Digite um valor: ')))
    print ('Valor adicionado com sucesso...')

    if element not in list:
        lista.remove (element)  
        print (lista)
    #else:
    #    lista.remove (element)  
    #    print('Removido!')
    #    print (lista)

    continuar = str (input ('Quer continuar? [S/N]: ')).strip().upper()
    #print (lista)
    #c == lista [:]
    #for c in lista

    
    if lista.append == lista.index(lista.append) :
        print ('Valor duplicado, não vou adicionar...')
        lista.remove ()        
    

    
    for c, lista.append[c] in lista.append :
        print ('Valor duplicado, não vou adicionar...')
        lista.remove (v)
    
    if continuar == 'S' :
        print (end = '')
        print (lista)
    elif continuar == 'N' : 
        break
        #c == 1
    elif continuar != 'SN' :
        print ('OPÇÃO INVÁLIDA!')
        #continuar = str (input ('Quer continuar? [S/N] ')).strip().upper()
    #elif continuar == 'S' :
    elif num != "1234567890" :
        print ('OPÇÃO INVÁLIDA!')

    
    #c = lista []
    if lista.append in lista:
        print ('Valor duplicado, não vou adicionar...')
    
"""




