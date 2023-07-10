"""
Crie um programa que tenha uma função fatorial() 
que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


    
def fatorial (num = 1, show=False) :
    """
    -> Calcula o Fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) mostra ou não a conta
    :return: O valor do Fatorial de un múmero num
    """
    f = 1
    for c in range (num, 0, -1) :
        if show:
            print (c, end = '')
            if c > 1 :
                print(' x ', end = '')
            else: 
                print(' = ', end = '')
        f *= c
    return f
    #print (r1, show = True)
    #print (r1)    
 
#r1 = fatorial (num)
#print (f'os resultados são: {r1}')


# PROGRAMA PRINCIPAL
num = int (input ('Digite um número: '))

r1 = fatorial (num)
#r1 = num
fatorial (num)


#print (r1)    
#print (r1, show = True)
print (fatorial(5, show=True))
print (fatorial(num, show=True))
#print (fatorial(5, show=False))
#print (fatorial(num, show=False))


help (fatorial)
