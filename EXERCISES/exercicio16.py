# numero que mostra a parte inteira digite 6.127  e a parte inteira é 6

num = float (input ( 'Digite o número: ' ))
import math
# outra forma é importar apenas o trunc
from math import trunc

inteiro = math.trunc(num)


print ( 'O valor digitado foi: {}  o inteiro é: {}' .format ( num, math.trunc( num )))

print ( 'O valor digitado foi: {}  o inteiro é: {}' .format ( num, trunc( num )))

print ( 'O valor digitado foi: {}  o inteiro é: {}' .format ( num, inteiro))

print ( 'O valor digitado foi: {}  o inteiro é: {}' .format ( num, int(num)))

