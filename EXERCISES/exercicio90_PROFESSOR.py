aluno = dict ()

aluno['nome'] = str (input ('Nome: '))
aluno['media'] = float (input (f'media: de {aluno["nome"]} '))

if aluno['media'] >= 7 :
    aluno ['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7 : 
    aluno['situacao'] = 'Recuperacao'
else :
    aluno['situacao'] = 'Reprovado'


print (aluno)

for k, v in aluno.items():
    print (f' - O {k} é igual a {v}')

    #print (f'A média é igual a {lista[0]["media"]}')
    #print (f'Situação é igual a {lista[0]["situacao"]}')