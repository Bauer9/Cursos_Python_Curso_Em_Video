# Interactive mode - help ()
#help ()


def contador (i, f, p) :
    """
    Funcao contador 
    :i - inicio
    :f - fim
    :p - passo
    Função criada por Felipe Bauer
    """
    c = i
    while c <= f :
        print (f'{c} ', end = '')
        c += p
    print ('Fim')

def somar (a, b, c) :
    s = a + b + c
    print (f'A soma vale {s}')
    
    
def somar2 (a=0, b=0, c=0) :
    s = a + b + c
    print (f'A soma2 vale {s}')

contador (2, 10, 2)


contador (2, 100, 10)


help (contador)



somar (3, 2, 5)
#somar (8, 4) #vai dar erro por que Função (DEF) "somar" precisa de 3 números para funcionar

somar2 (8, 4, 2)
somar2 (8, 4)
somar2 (8)
somar2 ()
somar2 (b=8, c=4)
somar2 (c=8, a=4)


#somar3 (8)

def teste () :
    x = 8 # variável Local - não existe fora da função teste
    n = 5
    print (f'Na função teste, n vale {n}')
    print (f'Na função teste, x vale {x}')

# PROGRAMA PRINCIPAL
n = 2 # variável Global
print (f'No programa principal n vale {n}.')
teste ()
#print (f'No programa principal, x vale {x}.') # Erro! a variável só existe dentro da função 

def teste2 (b) :
    a = 8 # variável local 
    b += 4
    c = 2
    print (f'A dentro vale {a}')
    print (f'B dentro vale {b}')
    print (f'C dentro vale {c}')


a = 5 # variável Global 
teste2 (a)
print (f'A fora vale {a}')

def funcao () :
    n1 = 4
    print (f'N1 dentro vale {n1}')


n1 = 2
funcao ()
print (f'N1 fora vale {n1}')



def teste3 (b) :
    global a1
    a1 = 8 # variável local 
    b += 4
    c = 2
    print (f'A1 dentro vale {a1}')
    print (f'B dentro vale {b}')
    print (f'C dentro vale {c}')
    

a1 = 3 # a variável dentro da função sobre-escreve as de fora dela por ser Global
teste3 (a1)
print (f'A1 fora vale {a1}')

def somarX (a=0, b=0, c=0) :
    s = a + b + c
    #print (f'A somaX vale {s}')
    return s

somarX (3, 2, 5)
somarX (3,2 )
somarX (3)

print (somarX (5, 2, 5))

r1 = somarX (3, 1, 5)
r2 = somarX (3,1 )
r3 = somarX (1)

print (f'meus calcúlos deram {r1}, {r2} e {r3}')
