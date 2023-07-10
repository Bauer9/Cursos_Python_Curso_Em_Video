# Vamos ver como fazer acesso a arquivos usando o Python.


import exercicio115_BASE



from exercicio115_BASE import cabecalho
from exercicio115_BASE import menu
from time import sleep
from exercicio115_BASE import arquivoExiste
from exercicio115_BASE import criarArquivo
from exercicio115_BASE import lerArquivo
from exercicio115_BASE import leiaInt
from exercicio115_BASE import cadastrar

arq = 'exercicio115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    print ('Arquivo criado com sucesso!')

"""
if arquivoExiste(arq):
    print ('Arquivo encontrado com sucesso!')
else:
    print ('Arquivo não encontrado! ')
    criarArquivo(arq)
"""


#cabecalho ('Sistema Arquivo v 1.0')

#menu (['opcao01', 'opcao02', 'opcao03'])

while True:
    resposta = menu (['Ver Pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #cabecalho ('Opção 1')
        # Opção de listar o conteúdo de um arquivo
        lerArquivo (arq)
    elif resposta == 2:
        #cabecalho ('Opção 2')
        #cadastrar uma noma pessoa
        cabecalho ('NOVO CADASTRO')
        nome = str (input ('Nome: '))
        idade = leiaInt ('Idade: ')
        cadastrar (arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print ('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)






"""
while True :
    num = str (input ('Sua Opção: '))


menu (num)
"""






