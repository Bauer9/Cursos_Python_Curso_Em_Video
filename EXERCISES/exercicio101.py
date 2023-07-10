#Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições.



from time import sleep


def voto (ano) :
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print (f'O ano atual é: {atual}')
    print ('-=' * 30)
    #elif media >= 5 and media <= 6.9 :
    if idade < 16 :
        print (f'A sua idade é de {idade} anos: NÃO VOTA')
    elif idade >+ 16 and idade < 18 or idade > 65:
        print (f'A sua idade é de {idade} anos: VOTO FACULTATIVO') 
    #elif idade >= 18 and idade < 65 :
    else: 
        print (f'A sua idade é de {idade} anos: VOTO OBRIGATÓRIO') 
    #elif idade >= 65 :
        #print (f'A sua idade é de {idade} anos: VOTO FACULTATIVO') 
    print ()

# PROGRAMA PRINCIPAL
ano = int (input ('Em que ano você nasceu? '))
voto (ano) #chamando a funcão "voto"



