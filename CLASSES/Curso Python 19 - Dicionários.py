dados = dict ()
dados = { 'nome': 'Pedro', 'idade': 25}

print ( dados['nome'])

print ( dados['idade'])

dados ['sexo'] = 'M' # adicionar o chaves sexo

print (dados)

del dados ['idade'] # apagar o chaves idade

print (dados)

filme = {'titulo':'Star Wars',
'ano':1977,
'diretor':'George Lucas' 
}

print (filme)
print (filme.values()) # valores
print (filme.keys())   #titulo ano diretor
print (filme.items()) # tudo


for k , v in filme.items() :
    print (f'O {k} é {v}')

print ('FIM')


# locadora = (dados[:])

print (locadora[0]['ano'])

print (locadora[1]["titulo"])


