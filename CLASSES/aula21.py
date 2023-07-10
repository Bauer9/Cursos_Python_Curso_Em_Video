def fatorial (num = 1) :
     f = 1
     for c in range ( num, 0, -1) :
        f *= c
     return f
 
 
 
r1 = fatorial (5)
r2 = fatorial (4)
r3 = fatorial ()
print (f'os resultados são: {r1}, {r2} e {r3}')
#print (fatorial(5, show=True))

def par (n=0) :
    if n  % 2 == 0 :
        return True
    else:
        return False
    
num = int (input ('Digite um número: '))
print (par(num))
if par (num) :
    print ('É par!')
else:
    print ('Não é par!')
    