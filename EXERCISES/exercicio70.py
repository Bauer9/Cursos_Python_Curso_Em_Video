""" Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 

"""


print ('-' * 31)
print (' ' *5,' LOJA SUPER BARATÃO', ' ' *5)
print ('-' * 31)
produto = preco = 0
total = 0
cont1000 = 0
menorPreco = 0
menorProduto = 0
contMenor = 0
contProdutos = 0
while True :
    produto =  str (input ('Nome do produto: '))
    preco =  int (input ('Preço: '))
    contProdutos += 1
    total = total + preco

    if preco > 1000 :
        cont1000 += 1
    if contProdutos == 1 :
        menorPreco = preco
        menorProduto = produto
    else:
        if preco < menorPreco :
            menorPreco = preco
            menorProduto = produto
            contMenor += 1


    continuar = ' '
    while continuar not in 'SN'  :
        continuar = str (input ('Quer continuar? [S/N] ')).strip().upper() 
    if continuar == 'N' :
        break


print (f'O total da compra foi R$ {total:.2f}.00')
print (f'Temos {cont1000} produtos custando mais de R$ 1000,00')
print (f'O produto mais barato foi {menorProduto} que custa R$ {menorPreco:.2f}')