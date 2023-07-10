# faça um app que leia o nome completo e mostre o primeiro e o último nome
# 
# EX: Ana maria de Souza
# primera: Ana
# última: Souza

nome = (input ('Qual é o seu nome completo?')).strip()
nome1 = nome.split()

print ('Prazer em te conhecer!')

print (nome1)

print ("Seu primeiro nome é: {}".format(nome1[0]))

#print ("Seu último nome é: {}".format(len(nome1))) # pegar a última posição

print ("Seu último nome é: {}".format(nome1[len(nome1)-1])) # última posição -1


