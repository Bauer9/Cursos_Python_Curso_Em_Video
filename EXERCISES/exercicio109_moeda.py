# aumentar, diminuir, dobro, metade

def aumentar (n, taxa = 10, format = False) :
    s = 0
    s = n + (n * taxa )/ 100
    #print (f'Aumentar {taxa} de {n} da {s} ')
    return s if format is False else moeda(s)

def diminuir (n, taxa = 25, format = False) :
    s = 0 
    s = n - (n * taxa) / 100
    #print (f'Diminuir {taxa} de {n} da {s} ')
    return s if format is False else moeda(s)

def dobro (n, format = False) :
    s = 0 
    s = n * 2
    #print (f'O dobro de {n} é {s} ')
    return s if format is False else moeda(s)

def metade (n, format = False) :
    s = 0 
    s = n / 2
    #print (f'A metade de {n} é {s} ')
    return s if format is False else moeda(s)

#num = 100
#taxa1 = 25
#taxa2 = 20

def moeda(preco = 0, moeda = 'R$') :
    return f'{moeda}{preco:5.2f}'.replace ('.', ',')






"""
aumentar (n, 20)
diminuir (n, 27)
dobro (n)
metade (n)
"""
"""
print (f'Aumentar {taxa1} de {num} da {aumentar(s)} ')
print (f'Diminuir {taxa2} de {num} da {diminuir(s)} ')
print (f'O dobro de {num} é {dobro(s)} ')
print (f'A metade de {num} é {metade(s)} ')   
"""

