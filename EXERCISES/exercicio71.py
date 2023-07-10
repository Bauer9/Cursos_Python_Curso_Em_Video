"""
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.



+ (Adição ou sinal positivo)	- Realiza a soma entre operandos - Adiciona o sinal de positivo ao número	- 10 + 7 - +4
- (Subtração ou sinal negativo)	- Realiza a subtração entre operandos - Adiciona o sinal de negativo ao número	- 10 - 7 - -4
* (Multiplicação)	Realiza a multiplicação entre operandos	3 * 4
/ (Divisão)	Realiza a divisão entre operandos	10 / 5
// (Divisão inteira)	Realiza a divisão entre operandos e a parte decimal do resultado	10 // 6
% (Módulo)	Retorna o resto da divisão entre operandos	4 % 2
** (Exponenciação)	Retorna um número elevado a potência de outro	4 ** 2

Operador	Conceito	Exemplo
>(Maior que)	Verifica se um valor é maior que outro	x > 5
<(Menor que)	Verifica se um valor é menor que outro	x < 5
== (Igual a)	Verifica se um valor é igual a outro	x == 5
!= (Diferente de)	Verifica se um valor é diferente de outro	x != 5
>= (Maior ou igual a)	Verifica se um valor é maior ou igual a outro	x >= 5
<= (Menor ou igual a)	Verifica se um valor é menor ou igual a outro	x <= 5
"""

print ('=' * 31)
print (' ' *5,' BANCO CEV', ' ' *5)
print ('=' * 31)

print ('=' *31)

cont = 0
sobra = 0
valor2 = ' '
ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
valor =  int (input ('Quanto você quer sacar: '))


while True :

    if valor >= ced50 :
        valor -= ced50
        cont50 += 1 
    if valor >= ced20 :
        valor -= ced20
        cont20 += 1 



        print (f'Total de {cont50:.0f} cédulas de 50 ')
        print (f'Total de {cont20:.0f} cédulas de 20 ')
        #print (f'Total de {cont10:.0f} cédulas de 10 ')
        #print (f'Total de {cont1:.0f} cédulas de 1 ')          
        print ('=' * 31)
    if valor == 0 :
        break

print ('Volte sempre ao BANCO CEV! Tenha um bom dia!')


    
"""
    if valor > 50 :
        sobra = valor / 50
        valor2 = valor % 50
        ced50 += sobra 
        print (f'{sobra:.0f}')
        print (f'{valor}')
        if valor2 > 20 :
            sobra = valor2 / 20
            valor2 =  valor2 % 20
            print (f'{sobra:.0f}')
            print (f'{valor2}')
            ced20 += sobra
        if valor2 > 10 :
            sobra = valor2 / 10
            valor2 =  valor2 % 10
            print (f'{sobra:.0f}')
            print (f'{valor2}')
            ced10 += sobra
        if valor2 > 1 :
            sobra = valor2 / 1
            valor2 =  valor2 % 1
            print (f'{sobra:.0f}')
            print (f'{valor2}')
            ced1 += sobra

            cont += 1

    print (f'Total de 50 cédulas de {ced50:.0f}')
    print (f'Total de 20 cédulas de {ced20:.0f}')
    print (f'Total de 5 cédulas de {ced10:.0f}')
    print (f'Total de 1 cédulas de {ced1:.0f}')    
    print ('=' * 31)

print ('Volte sempre ao BANCO CEV! Tenha um bom dia!')
"""

#print (f'{sobra:.0f}')
#print (f'{valor}')


