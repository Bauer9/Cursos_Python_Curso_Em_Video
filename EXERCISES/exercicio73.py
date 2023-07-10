"""
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
"""


lista = ('Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Brasília', 'Salvador', 'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus', 'Belém', 'Goiânia', 'Chapecoense', 'Natal', 'Florianópolis', 'Vitória', 'Aracaju', 'Maceió', 'Campo Grande', 'Cuiabá')

print (f'lista de Times do brasileirão: {lista}')
print ('-=' * 15)
# A
print (f'Os seis primeiros colocados são: {lista[0:5]}')
print ('-=' * 15)
#B
print (f'Os últimos 4 colocados: {lista[-4:]}')
print ('-=' * 15)
#C
print (f'Times em ordem alfabética: {sorted(lista)}') # ordem alfabética
print ('-=' * 15)
# D
print (f'O Chapecoense está na:',  lista.index ('Chapecoense')+1, 'posição')
print ('-=' * 15)
#print (c.index(2)) # só mostra a primeira posição do 2, ele ignora o segundo 2
#print (frase.find ('Vídeo'))