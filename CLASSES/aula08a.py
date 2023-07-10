#import math
from math import sqrt, floor
num = int (input ('Digite um número'))

raiz = math.sqrt(num)


print('A raiz de {} é igaual a {:.2f}'.format(num, math.floor(raiz)))
print('A raiz de {} é igaual a {:.2f}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igaual a {:.2f}'.format(num, raiz))

"""
ceil para cima
                floor para baixo
                trunc truncar


"""