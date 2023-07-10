# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import exercicio108_moeda 

num = float (input ('Digite um número: '))
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

print (f'Aumentar {taxa1}% de {exercicio108_moeda.moeda(num)} da: {exercicio108_moeda.moeda(exercicio108_moeda.aumentar(num, taxa1))} ')
print (f'Diminuir {taxa2}% de {exercicio108_moeda.moeda(num)} da: {exercicio108_moeda.moeda(exercicio108_moeda.diminuir(num, taxa2))} ')
print (f'O dobro de {exercicio108_moeda.moeda(num)} é: {exercicio108_moeda.moeda(exercicio108_moeda.dobro(num))} ')
print (f'A metade de {exercicio108_moeda.moeda(num)} é: {exercicio108_moeda.moeda(exercicio108_moeda.metade(num))} ')   
    