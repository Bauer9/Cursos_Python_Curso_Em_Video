# somar os angulos do triângulo e achar a hipotenuza

#import math
import math

#ou impotar so a hipotenusa ou outros comandos  
from math import sqrt, hypot

math.hypot # carrega a função da hiponenuza


co = float ( input ( 'Digite o cateto oposto: ' ))
ca =  float ( input ( 'Digite o cateto adjacente: ' ))
hipo = sqrt ( co*co + ca*ca )

# outra maneira com matemática
hi = ( co ** 2 + ca ** 2) ** (1/2)

# com o math Hypot
hi2 = math.hypot(co,ca)

print('a Hipotenuza é:{}'.format(hipo))

print('a Hipotenuza é:{:.2f}'.format(hi))

print('a Hipotenuza é:{:.2f}'.format(hi2))


