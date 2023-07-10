# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str (input ('Informe o sexo (M/F): ')).strip() .upper()[0]
while sexo not in 'MmFf' :
    sexo = str (input ('Informe o sexo (M/F): ')).strip() .upper()[0]
    #print (sexo)
    print ('Sexo invalidos. ', end ='' )
print ('\n',sexo)
print ('Sexo Masculino registrado com Sucesso, fim')


