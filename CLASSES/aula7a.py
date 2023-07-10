#print ('4'+'2')

"""
nome = input ('Qual é o seu nome?')

print('Prazer em te conhecer {:^20}!'.format(nome))
"""

n1 = int (input('Um valor:'))
n2 = int (input('Outro valor:')) 

soma = n1+n2

m = n1 * n2

d = n1 / n2

di = n1 // n2

e = n1 ** n2

# duas casas flutuantes depois da virgula da divisão: :.2f
# quebra de linha no print: \n
# não ter qubra de linha: end=" " 

print ('A soma é {}, \no produto é {} \n e a divisão é {:.2f} \n '.format (soma, m, d), end=" ")
print ('Divisão inteira é {}, potencia é {}'.format (di,e))



