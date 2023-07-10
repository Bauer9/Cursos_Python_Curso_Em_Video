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

valor =  int (input ('Quanto você quer sacar: '))

total = valor
ced = 50
totced = 0

while True :
    if total >= ced :
        total -= ced
        totced += 1
    else :
        if totced > 0 :
            print (f'Total de {totced} cédulas de {ced}')
        if ced == 50 :
            ced = 20
        elif ced == 20 :
            ced = 10
        elif ced == 10 :
            ced = 1
        totced = 0
        if total == 0 :
            break




print ('Volte sempre ao BANCO CEV! Tenha um bom dia!')



