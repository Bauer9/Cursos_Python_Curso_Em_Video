def soma2 (a,b) :
    print (f'A = {a} e B = {b}')
    s = a + b
    print (f'A soma A + B = {s}')

def soma (a,b) :
    s = a + b
    print (s)
    
def contador (*num) :
    print (num)
    
def contador2 (*num) :
    for valor in num:
        print (f' {valor} ', end='')
    print ('FIM!')

def contador3 (*num) :
    tam = len(num)
    print (f'Recebi os valores {num} que não ao todo {tam} números')

def dobra (lista) :
    pos = 0
    while pos<len(lista):
        lista[pos]*=2
        pos += 1

def soma3 (*valores) :
    s = 0
    for num in valores:
        s += num
    print (f'Somando os {valores} temos {s}')

a = 4
b = 5
s = a + b
print (s)
a = 8
b = 9
s = a + b
print (s)
a = 2
b = 1
s = a + b
print (s)

soma (4, 5)
soma (8, 9)
soma (2, 1)

soma (a=3, b=1)
soma2 (b=5, a=2)

contador (2, 1, 7)
contador (8,0 )
contador (4, 4, 7, 6, 2)

contador2 (2, 1, 7)
contador2 (8,0 )
contador2 (4, 4, 7, 6, 2)

contador3 (2, 1, 7)
contador3 (8,0 )
contador3 (4, 4, 7, 6, 2)

valores = [7,2,5,0,4]
print (f'Valores {valores}')
dobra(valores)
print(f'Valores Dobrados {valores}')

soma3 (8, 8)
soma3 (2, 1)