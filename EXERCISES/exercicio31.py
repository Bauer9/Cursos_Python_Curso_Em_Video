# Distancia de uma viagem em KM
# calcule o preço da pasagem do onibus
# R$ 0,50 por km para viagens até 200 km 
# R$ 0,45 para viagens mais longas
# 


distancia = int (input('Qual a ditancia da viagem?'))

"""
if km <= 200:
    print ('O custo da viagem > que 200KM é de R$ 0.50 km, então vai custar: R$ {:.2f}' .format(km* 0.50))
else:
    print ('O custo da viagem < que 200KM é de R$ 0.45 km, então vai custar: R$ {:.2f}' .format(km* 0.45))

"""


"""

# operador ternário ou IF line
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
"""

if distancia <= 200 :
    preco = distancia * 0.50
else:
    preco = distancia * 0.45


print ('O custo da viagem é de: {}' .format(preco))
