#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list ()
#n=0

for n in range (0, 5) :
    num = int (input ('Digite um número: '))

    if n == 0 or num > lista [-1]:
        lista.append (num) 
        print (lista)
    # Elif faz o mesmo procedimento que o IF, professor juntou os 3 com o or
    #elif num > listalen(lista)-1 : # ou n > lista[-1] :
    #    lista.append (num) 
    #    print (lista)
    else:
        pos = 0
        while pos < len(lista) :
            if num <= lista[pos] :
                lista.insert(pos, num)
                break
            pos += 1

print ('=-' * 20)    
print (f'Os valores digitados foram: {lista}')


#num.index (3)
    #if n > 0 :
    #    lista.append (num) 
    #    print (lista)    
"""
    if num < lista.append (0) :
        lista.insert (0, num) 
        print (lista)     
        
    n += 1    
""" 

"""
    if lista.append (num) > lista.index (n) :
        #inserir o valor Zero na posição 2
        #num2.insert(2, 0)
        lista.append(num)

    if lista.append (num) < lista.index (n) :
        #inserir o valor Zero na posição 2
        #num2.insert(2, 0)
        lista.insert(0, num)
"""
    



