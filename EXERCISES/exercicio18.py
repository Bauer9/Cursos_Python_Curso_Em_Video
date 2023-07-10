# pelo angulo achar o seno, cosseno e a tangente

import math
# from math import sin, pi, cos, radians

angulo = float ( input( 'Digite o primeiro número: '))
seno = math.sin( math.radians (angulo))
print ( 'O angulo de {} tem o SENO de {:.2f}' . format ( angulo, seno ))
cosseno = math.cos( math.radians (angulo))
print  ('O angulo de {} tem o COSSENO de {:.2f}' . format ( angulo, cosseno ))

tangente = math.tan( math.radians (angulo))
print ('O angulo de {} tem a TANGENTE de {:.2f}' . format ( angulo, tangente ))


# angle = math.sin(math.pi/4)



