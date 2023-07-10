# programa de emprestimo bancario
# Qual o valor da casa?
# O salário
# Quantos anos vai pagar?
# O valor da prestação não pode exceder 30% do salário, se exceder o valor é negado


imovel = float (input ('Qual o valor do imóvel? '))
sal = float (input ('Qual o seu salário? '))
anos = int (input ('Em quantos anos quer pagar? '))

prestacao = imovel / (anos*12 )
minimo = sal * 30 /100

if prestacao <= minimo :
   resultado = 'Aprovado!'
else: 
   resultado = 'negado!'


print ('O valor da prestação é de: R$ {:.2f}, em {} de pagamento, de acordo com 1/3 do seu salário R$ {} o Emprestimo foi: {}' . format( prestacao, anos, minimo ,resultado))

