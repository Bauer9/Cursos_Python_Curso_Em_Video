#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

"""
from ex112.utilidades import moeda

p = float (input ('Digite o preço: R$'))
moeda.resumo (p)

moeda.resumo (p, 20, 80)

#resumo (num)
"""

from COURSES.CURSO_EM_VIDEO_120H.EXERCISES.ex112.utilidades import moeda
from COURSES.CURSO_EM_VIDEO_120H.EXERCISES.ex112.utilidades import dado
#from PYTHON_COURSE_CURSO_EM_VIDEO_120H.ex112.utilidades import moeda

p = dado.leiaDinheiro ('Digite o preço: R$ ')
#p = float (input ('Digite o preço: R$'))
moeda.resumo (p)


moeda.resumo (p, 20, 80)
#resumo (num)
