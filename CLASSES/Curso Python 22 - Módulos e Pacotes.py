

#""" # coloca # 
import COURSES.CURSO_EM_VIDEO_120H.CLASSES.Curso_Python22_uteis # MANEIRA RECOMENDADA POR DIMINUIR CONFLITOS DE IMPORTACOES COM DUAS FUNCOES DE MESMO NOME

num = int (input ('Digite um valor: '))

fat = COURSES.CURSO_EM_VIDEO_120H.CLASSES.Curso_Python22_uteis.fatorial (num)

print (f'O fatorial de {num} é {fat}')
print (f'O dobro de {num} é {COURSES.CURSO_EM_VIDEO_120H.CLASSES.Curso_Python22_uteis.dobro(num)}')
print (f'O triplo de {num} é {COURSES.CURSO_EM_VIDEO_120H.CLASSES.Curso_Python22_uteis.triplo(num)}')

#print (f'O triplo de {num} é {triplo}') # erro imprime um valor interno dp Python

# ou

"""

from COURSES.CURSO_EM_VIDEO_120H.CLASSES.Curso_Python22_uteis import fatorial, dobro, triplo

fat = fatorial (num)

print (f'O fatorial de {num} é {fat}')
print (f'O dobro de {num} é {dobro(num)}')
print (f'O triplo de {num} é {triplo(num)}')
""" # tira #




