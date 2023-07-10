#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.


from datetime import date
clientes = dict ()
cadastro = dict ()

"""
nome = str (input ('Nome: '))
nasc = int (input ('Ano do nascimento: '))
cart = int (input ('Carteira de trabalho: (0 não tem): '))
"""



for i in range (0, 1) :
    cadastro['nome'] = str (input ('Digite o nome: '))
    cadastro['ano'] = int (input ('Ano de nascimento: '))
    cadastro['CTPS'] = int (input ('Carteira de trabalho (0 não tem): '))
    
    atual = date.today().year
    idade = atual - cadastro['ano'] 
    # cadastro.append (idade.copy())
    cadastro ['idade'] = idade

    if cadastro['CTPS'] == '0' :
        for k, v in enumerate (cadatro) :
            print (f'- {k} tem o valor {v}')
    else:
        cadastro['ano contratacao'] = int (input ('Ano da contratação: '))
        cadastro['salario'] = int (input ('Salário: '))
        aposentadoria = (35 - (atual - cadastro['ano contratacao'] ) ) + atual
        cadastro ['aposentadoria'] = aposentadoria
        #aposentadoria2 

print (f'{cadastro["nome"]} tem {cadastro["idade"]} anos. ')

print ('-=' * 30)
for k, v in cadastro.items() : 
    print (f'- {k} tem o valor {v}')
    #print (f' - O {k} é igual a {v}')

