

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


"""



lista = dict ()
cadastro = dict ()

for i in range (0, 1) :
    cadastro['nome'] = str (input ('Digite o nome: '))
    cadastro['media'] = int (input ('Digite a média: '))
    if cadastro['media'] >= 7 :
        cadastro['situacao'] = 'Aprovado'
    elif 5 <= cadastro['media'] <7 :
        cadastro['situacao'] = 'Recuperação'
    else :
        cadastro['situacao'] = 'Reprovado'
    lista.append(cadastro.copy())
"""
for k, v in cadastro.items():
    print (f'O {k[0]} é igual a {v[0]} ')
    print (f'{k[1]} é igual a {v[1]}  ')
    print (f'Situação {k[2]} é igual a {v[2]}')
print (lista)
"""
#for k, v in lista.items():
    #print (f'O {k} é igual a {v}')
    #print (f'A média é igual a {lista[0]["media"]}')
    #print (f'Situação é igual a {lista[0]["situacao"]}')


print (f'O Nome é igual a {lista[0]["nome"]}')
print (f'A média é igual a {lista[0]["media"]}')
print (f'Situação é igual a {lista[0]["situacao"]}')
#print (lista)




