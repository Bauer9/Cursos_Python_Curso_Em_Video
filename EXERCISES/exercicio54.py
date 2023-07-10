# Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date

atual = date.today().year


cont = 0
cont2 = 0
for c in range (1, 8) :
    nasc = int (input ('Data de nascimento {}: ' .format (c)))
    idade = atual - nasc
    

    if idade >=21 : 
        #print ('Data de nascimento {} data {}' .format (c, nasc))
        cont += 1
    else:
        cont2 += 1
print ('Ao todo são {} pessoas são menores' .format (cont2))
print ('E {} pessoas já atingiram a maioridade' .format (cont))
print ('FIM')