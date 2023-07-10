def leiaInt (msg) :
    while True:
        try:
            a = int (input('Digite um número Inteiro: '))
        except (ValueError, TypeError):  # mais e um erro usar ()
            print('\033[031mERRO: Digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt) :
            print('\033[031mERRO: Entrada de dados interrompida pelo usuário.\033[m')
            return '0'
        else:
            return a

def leiaFloat (msg) :
    while True:
        try:
            a = float(input('Digite um número Real: '))
        except (ValueError, TypeError):  # mais e um erro usar ()
            print('\033[031mERRO: Digite um número Real válido.\033[m')
        except (KeyboardInterrupt) :
            print('\033[031mERRO: Entrada de dados interrompida pelo usuário.\033[m')
            return '0'
        else:
            return a


num = leiaInt ('Digite um valor: ')
num2 = leiaFloat ('Digite um Real:  ')
print (f'O valor digitado foi {num} e o Real foi {num2}')




"""
try :
    a = float (input ('Digite um número Inteiro: '))

except (ValueError, TypeError) : # mais e um erro usar ()
    print ('Tivemos ma problema com os tipos de dados que voc6e digitou.')


try:
    b = float(input('Digite um número Real: '))

except (ValueError, TypeError):
    print('Tivemos ma problema com os tipos de dados que voc6e digitou.')

#finally:

print (f'o valor inteiro digitado foi {a} e o real foi {b}')
"""

