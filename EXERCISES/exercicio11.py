#largura e altura da parede, calcule a área e a quantidadede tinta necssária para pinta-lá,
# sabendo que cada litro de tinta pinta 2 metros quadrados


larg = float (input ('Qual a largura da parede?'))
alt= float (input ('Qual a a altura da parede?'))

area = larg * alt
tinta = area /2

print('A área em m2 é: {}m \nVocê vai precisar de {} litros de tinta para pintar essa parede'.format(area,tinta))



