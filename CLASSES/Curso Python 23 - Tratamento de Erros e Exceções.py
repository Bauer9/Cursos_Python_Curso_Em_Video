
n = int (input ('Número: '))
print (f'Você digitou o número {n}') # Se digitar letras vai dar uma Exceção (não é um erro) só aceita números

#print (x) # EXCEÇÃO - ERRO SEMANTICO, a variável 'x' não existe

"""
a = int (input ('Nemerador: '))
b = int (input ('Denominador: '))
r = a / b # Se colocar '0' zero da uma EXCEÇÃO - ZeroDivisionError: division by zero não existe divisão por zero
"""

"""
Resolver exceções

try:
    operação
except:
    falhou # resolver o que vai aocntecer quando encontrar a exceção
else: 
    deu certo
finally:
    acontece no acerto ou na falha acerto / falha
"""
try :
    a = int (input ('Nemerador: '))
    b = int (input ('Denominador: '))
    r = a / b  # Se colocar '0' zero da uma EXCEÇÃO - ZeroDivisionError: division by zero não existe divisão por zero
#except :
#    print ('infelizmente tivemos um problema :(')
#except  Exception as erro:
#    print (f'O problema encontrado foi {erro.__class__}')
except (ValueError, TypeError) : # mais e um erro usar ()
    print ('Tivemos ma problema com os tipos de dados que voc6e digitou.')
except ZeroDivisionError :
    print ('Não é possível dividir por zero!')


else :
    print (f'O resultado é {r:.1f}')
finally :
    print ('Volte sempre muito obrigado')
