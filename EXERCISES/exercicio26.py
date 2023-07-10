# digite uma frase e leia essa frase
# quantas vezes aparece a letra "a"
# Em que posição aparece a primeira
# Em que posição aparece a última vez

frase = str(input('Digite uma frase:')) .upper() .strip() 

print ( 'O tamanho da frase é: {}' .format(len(frase)))
#print ( 'Tem {} na frase ' .format(frase.count('A')))

print ( 'A letra A aparece {} vezes na frase'.format(frase.count('A')  ))

print ( 'A primeira posição dela é {}, a última posição é {}' .format(frase.find('A')+1, frase.rfind('A')+1)  )


