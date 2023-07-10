# https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=31

# fatiamento de STRING tem 21 casas

Strings são imutáveis, só muda se usar uma função apra isso, exemplo - Replace


frase [9:13]  - Manipulating [9:13] # ele pega do 9 ao 12 - o último valor não entra na contagem

frase [9:21]    -  para ler a última casa 

frase [9:21:2]  -  pega do 9 ao 20 pulando de 2 em 2

frase [:5]  -   ele pega do 0 a 4

frase [15:]  -   indicou o início que é o 15 e vai até o final da string que é o 20

frase[9::3]  -  começa no 9 e vai até o final e depois pula de 3 em 3 casas

len(frase) - função len - o comprimento da frase

frase.count('o') - quantas letras o minúsculas tem na frase

frase.count('o',0,13) entre o 0 e o 12 tem apenas uma letra or

frase.find('deo') quantas vezes encontrou o 'deo', mostra em que momento começou - casa 11

frase.find('Android') - quando não existe ele retorna -1 = ou seja não foi encontrada

'Curso' in frase - escreve true se tiver ou false para não

mudar estring atrvés de método:
frase.replace('Python' , 'Android') substitiu o Pyhton por Android de forma secundária

frase.upper() ou lower - maiúscula ou minúscula, Upper joga as letras que naao estao maiúsculas para maiúsculas e co contrário com o lower
frase.lower() 

frase.capitalize() tudo para minúsculo e apenas a primeira ele coloca em maisúsculo

frase.title() transforma a primeira letra de cada palavra em maisúsculo

frase.strip() remove espaços inúteis do inicio e do final, não os que separa palavras

funcão "R" right - muito usada em Python só remov do lado direito

funcão "L" left - muito usada em Python só remove do lado esquerdo

frase.rstrip()  remove apenas os espaços que estão na direita

frase.split() - gera uma lista nova para cada palavra - ele divide os espaço entre as palavras em listas

'-'.join(frase) junta todas as strings e cria uma nova com tudo chamada frase








