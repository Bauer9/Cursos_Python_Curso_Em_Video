# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""
frase.strip() remove espaços inúteis do inicio e do final, não os que separa palavras

funcão "R" right - muito usada em Python só remov do lado direito

funcão "L" left - muito usada em Python só remove do lado esquerdo

frase.rstrip()  remove apenas os espaços que estão na direita

frase.split() - gera uma lista nova para cada palavra - ele divide os espaço entre as palavras em listas

'-'.join(frase) junta todas as strings e cria uma nova com tudo chamada frase

len(frase) - função len - o comprimento da frase

"""


frase = str (input ('Digite uma frase: ')).strip().upper()
#lens = len(frase)
#joins = join(frase)

#frase = frase.replace(' ','')

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#print ('{}' .format(frase))
#print ('{}' .format(palavras))
#print ('{}' .format(junto))

for letra in range (len(junto) -1, -1, -1) :
    inverso += junto[letra]
    #print (junto, inverso)
if inverso == junto :
    print ('SImmm é um palíndromo!')
    
else:
    print ('Não é um palíndromo!')




#for c in range (0, lens, -1) :

    #frase = frase.replace(' ','')
    #print ('{}' .format(frase))    

#print (frase[::-1])


#print ('SImmm é um palíndromo!')
#print ('Não é um palíndromo!')