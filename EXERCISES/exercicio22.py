
#crie um programa que leia o nome completo da pessoa e mostre:
# todas as letras maiúsculas
# todas minúsculas
# quantas letras term sem contar espaços
# quantas letras tem o primeiro nome
# 



nome = str (input ( 'Digite seu nome completo: ' )).strip()

SemEsp = nome.replace(' ' , '')

dividido = nome.split()

# frase.strip() remove espaços inúteis do inicio e do final, não os que separa palavras

print ('Em maiúsculo {}'.format(nome.upper()))

print ('Em minúsculas {}'.format(nome.lower()))

# minha solução
#print ('O nome sem os espaços {} tem {} letras ' .format (SemEsp , len(SemEsp)) )

print ('O nome sem os espaços é {} tem  letras ' .format (len(nome) - nome.count(' ')) )

#print ('O primeiro nome que é {}, tem {} letras'.format(nome[0:4] , len(nome[0:4])))

# minha solução
print ('O primeiro nome que é {} tem {} letras'.format(dividido[0] , len(dividido[0])))

print ('O primeiro nome tem {} letras' . format (nome.find (' ')))
