# (
# pergunte o salário do funcionário e calcule o aumento
# salários superiores a 1.250 acrescente 10%
# para iguais ou inferiores aumente 15%
# )
# 

salario = int (input ('Digite o seu salário: '))

#salario = aumento


if salario > 1250:
    novo = salario + salario* 10 / 100
    print ('Seu salário novo com aumento de 10%: {}' .format (novo))
else:
    novo = salario + salario* 15 / 100
    print ('Seu salário novo com aumento de 15%: {}' .format (novo))