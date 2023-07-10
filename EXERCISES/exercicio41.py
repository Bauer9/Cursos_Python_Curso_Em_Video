"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

from datetime import date
nasc = int (input ('Digite o ano de nascimento: '))

atual = date.today().year
idade = atual - nasc

print ('Você nas no ano de {} e tem {} anos' .format(nasc, idade))

if idade <= 9 :
    print ('Você nasceu em {} tem {} anos é MIRIM' .format(nasc, idade))
   # if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
elif idade > 9  :
    print ('Você nasceu em {} tem {} anos é INFANTIL' .format(nasc, idade))
elif idade >= 14 and idade < 19  :
    print ('Você nasceu em {} tem {} anos é JÜNIOR' .format(nasc, idade))
elif idade >= 19 and idade < 25  :
    print ('Você nasceu em {} tem {} anos é SENIOR' .format(nasc, idade))
elif idade >= 25 :
    print ('Você nasceu em {} tem {} anos é MASTER' .format(nasc, idade))
