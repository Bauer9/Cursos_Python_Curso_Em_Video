"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""

print ('{:=^40}' . format('LOJAS GUANABARA'))

preco = float (input ('Preço das compras: '))

print ('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão
''')

opcao = int (input ('Qual é a sua opção? '))
if opcao >4 :
    print ('OPCÃO INVALIDA, tente novamente')


if opcao == 1 :
    total = preco - (preco *10/100)
  
    print ('Opção: [ {} ], à vista dinheiro/cheque com 10% de desconto, valor final: R$ {} ' .format (opcao, total))
elif opcao == 2 :
    total = preco - (preco *5/100)
   
    print ('Opção: [ {} ], à vista no cartão, com desconto de 5%, valor final: R$ {}  ' .format (opcao, total))
elif opcao == 3 :
    total = preco
    parcelas = int (input ('Quantas parcelas? '))
    parcelado = preco / parcelas 
    cartao = preco / 2
    print ('Opção: [ {} ], {} Parcelas de R$ {:.2f},  2x no cartão de {:.2f}, valor final: R$ {}' .format (opcao, parcelas, parcelado, cartao, total))
elif opcao == 4 :
    total = preco + (preco *20/100)
    parcelas = int (input ('Quantas parcelas? '))
    parcelado = preco / parcelas
    cartao = preco / 3
    print ('Opção: [ {} ] {} Parcelas de R$ {:.2f} com juros de 20%,  3x no cartão de {:.2f}, valor final: R$ {}' .format (opcao, parcelas, parcelado, cartao,  total))
