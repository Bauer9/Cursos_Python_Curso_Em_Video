# pergunte quantos kilometros e quantos dias vcalugou esse carro. calcule o valor final,  dia alugado é 60,00 e do Km rodado é 0,15

dias = int (input ( 'Quantos dias o carro foi alugado?' ))
km = float (input ( 'Quantos km ele percorreu?' ))

valorfinal = (dias * 60) + (km * 0.15)


print ('o carro foi alugado por {} dias e que rodou {}km, o valor é de: R${:.2f}'.format(dias, km, valorfinal))




