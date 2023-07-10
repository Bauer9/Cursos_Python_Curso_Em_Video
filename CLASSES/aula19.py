"""
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print (pessoas)

print (pessoas['nome'])

print (f'{pessoas["nome"]} tem {pessoas["idade"]} anos')


print (pessoas.keys())
print (pessoas.values())
print (pessoas.items())

for k in pessoas.keys() :
    print (f'Print keys {k} ')

for v in pessoas.values() :
    print (f'Print values {v} ')

for k, v in pessoas.items() :
    print (f'Print items {k} = {v} ')

print ('Apagando o "sexo"')
del pessoas ['sexo']

pessoas ['nome'] = 'leandro' #mudar o nome


for k, v in pessoas.items() :
    print (f'Print items {k} = {v} ')
"""
"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ' }
estado2 = {'uf': 'São Paulo', 'sigla': 'SP' }

brasil.append (estado1)
brasil.append (estado2)

print (estado1)
print (estado2)
print (brasil)
print (brasil[0])
print (brasil[0]  ['uf'])
print (brasil[1]  ['sigla'])
print (brasil[1])
"""
estado = dict ()
brasil = list ()

for c in range (0, 3) :
        estado['uf'] = str (input ('Unidade Federativa: '))
        estado ['sigla'] = str (input ('Sigla do estado: '))
        brasil.append(estado.copy())
print (brasil)
for e in brasil :
    print (f'{e}')
    for k, v in e.items() :
        print (f'o campo {k} tem valor {v}.' )
    for v in e.values() :
        print (f'{v}', end = '')



