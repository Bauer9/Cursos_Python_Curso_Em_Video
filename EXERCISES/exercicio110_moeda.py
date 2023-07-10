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

def moeda(n = 0, moeda = 'R$') :
    return f'{moeda}{n:5.2f}'.replace ('.', ',')


def resumo (n = 0, taxaa = 10, taxar = 5) :

    print ('-' * 30)    
    print ('RESUMO DE VALOR'.center(30))
    print ('-' * 30)    
    
    print (f'Preço analisado: \t{moeda(n)}')
    print (f'Dobro do preço: \t{dobro (n, True)} ')
    print (f'Metade do preço: \t{metade (n, True)} ')
    print (f'{taxaa}% de aumento: \t{aumentar (n, taxaa, True)} ')
    print (f'{taxar}% de Redução:  \t{diminuir (n, taxar, True)} ')
   
    print ('-' * 30)    



#aumentar (num, 20)
#diminuir (num, 27)
#dobro (num)
#metade (num)


#resumo (num)

