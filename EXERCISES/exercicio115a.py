# Vamos criar um menu em Python, usando modularização.


import exercicio115a_interface
from exercicio115a_interface import cabecalho
from exercicio115a_interface import menu
from time import sleep

#cabecalho ('Sistema Arquivo v 1.0')

#menu (['opcao01', 'opcao02', 'opcao03'])

while True:
    resposta = menu (['Ver Pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho ('Opção 1')
    elif resposta == 2:
        cabecalho ('Opção 2')
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






