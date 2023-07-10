# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""ano = int (input ('Ano de nascimento: '))

idade = 2023 - ano


 MINHA SOLUÇÃO
if idade < 18 :
    faltam = 18 - idade
    alistamento = faltam + 2023
    print ('Quem nasceu em {} tem {} anos em 2023.' .format(ano, idade))
    print ('Ainda faltam {} para o alistamento' .format(faltam))
    print ('Seu alistamento será em {}' .format (alistamento))
elif idade > 18 :
    faltam = idade - 18
    alistamento = 2023 - faltam
    print ('Quem nasceu em {} tem {} anos em 2023.' .format(ano, idade))
    print ('Você já deveria ter se alistado a {} anos' .format(faltam))
    print ('Seu alistamento foi em {}' .format (alistamento))
elif idade == 18 :
    print ('Quem nasceu em {} tem {} anos em 2023.' .format(ano, idade))
    print ('Você precisa se alistar IMEDIATAMENTE')
"""

from datetime import date

atual = date.today().year
nasc = int (input ('ano de nascimento: '))
idade = atual - nasc


if idade == 18 :
    print ('Quem nasceu em {} tem {} anos em 2023.' .format(nasc, idade))
    print ('Você precisa se alistar IMEDIATAMENTE')
elif idade < 18 :
    saldo = 18 - idade
    print ('Quem nasceu em {} tem {} anos em 2023.' .format(nasc, idade))
    print ('Ainda faltam {} ano para o alistamento' .format(saldo))
    ano = atual + saldo
    print ('Seu alistamento será em {}' .format (ano))
elif idade > 18 :
    saldo = idade - 18
    print ('Quem nasceu em {} tem {} anos em 2023.' .format(nasc, idade))
    print ('Você já deveria ter se alistado a {} anos' .format(saldo))
    ano = atual - saldo
    print ('Seu alistamento foi em {}' .format (ano))


