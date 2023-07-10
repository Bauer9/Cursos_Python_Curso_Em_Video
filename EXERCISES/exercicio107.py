# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

#from exercicio107_moeda import aumentar, diminuir, dobro, metade
import exercicio107_moeda 

num = int (input ('Digite um número: '))
taxa1 = int (input ('Digite a taxa de aumentar: '))
taxa2 = int (input ('Digite a taxa de diminuir: '))

#n = 23
#taxa1 = int (taxa1i)
#taxa2 = int (taxa2i)

"""
aumentar (num, taxa1)
diminuir (num, taxa2)
dobro (num)
metade (num)
"""

print (f'Aumentar {taxa1}% de {num} da {exercicio107_moeda.aumentar(num, taxa1)} ')
print (f'Diminuir {taxa2}% de {num} da {exercicio107_moeda.diminuir(num, taxa2)} ')
print (f'O dobro de {num} é: {exercicio107_moeda.dobro(num)} ')
print (f'A metade de {num} é: {exercicio107_moeda.metade(num)} ')   
    
    