# Valor do produto com 5% de desconto
preco= float(input('Digite um preço do produto:'))

#desconto de 5%
desconto = (preco*0.05)

# outro jeito de fazer
desconto = preco*5/100
valordesconto = preco-desconto


print ('O produto que custava R${} \ncom desconto de 5%: {} \nO preço final com desconto é de: {}'.format(preco, desconto, valordesconto))


