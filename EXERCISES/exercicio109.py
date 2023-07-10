"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

import exercicio109_moeda

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

print (f'Aumentar {taxa1}% de {exercicio109_moeda.moeda(num)} da: {(exercicio109_moeda.aumentar(num, taxa1, True))} ')
print (f'Diminuir {taxa2}% de {exercicio109_moeda.moeda(num)} da: {(exercicio109_moeda.diminuir(num, taxa2, True))} ')
print (f'O dobro de {exercicio109_moeda.moeda(num)} é: {(exercicio109_moeda.dobro(num, True))} ')
print (f'A metade de {exercicio109_moeda.moeda(num)} é: {(exercicio109_moeda.metade(num, True))} ')
print (f'Diminuir 2 33% {taxa2}% de {exercicio109_moeda.moeda(num)} da: {(exercicio109_moeda.diminuir(num, 33, True))} ')





