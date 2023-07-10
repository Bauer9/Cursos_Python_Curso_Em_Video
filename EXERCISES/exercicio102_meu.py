def fatorial (num) :
    resultado = 1
    for c in range (num, 0 , -1) :
        print (c, end = '')
        if c > 1 :
            print (' x ', end = '')
        else: 
            print (' = ', end = '')
        #global resultado
        resultado *= c
    print (resultado)
    
    
    
#fatorial (3)
"""
num = int (input ('Digite um número: '))
resultado = 1
for c in range (num, 0 , -1) :
    print (c, end = '')
    if c > 1 :
        print (' x ', end = '')
    else: 
        print (' = ', end = '')

    resultado *= c

print (resultado)
"""

num = int (input ('Digite um número: '))

fatorial (num)
#print (resultado)
#print (fatorial(num))





