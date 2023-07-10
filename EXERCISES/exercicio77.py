# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


 
#lista = ('Rio de Janeiro', 'Sao Paulo', 'Belo Horizonte', 'Brasilia', 'Salvador', 'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus', 'Belem', 'Goiania')


"""

def vowel_count(str):
    # Creating a list of vowels
    vowels = "aeiouAEIOU"
     
    # Using list comprehension to count the number of vowels in the string
    count = len([char for char in str if char in vowels])
     
    # Printing the count of vowels in the string
    print("No. of vowels :", count)
 
# Driver code
str = "GeeksforGeeks"
 
# Function Call
vowel_count(str)
"""
#a

"""# AINDA NÃO FUNCIONOU 
x = ('a', 'e', 'i', 'o', 'u')

thisdict = dict.fromkeys(x)

print(thisdict)

#d = {}.fromkeys([1, 2, 3], "NULL")

"""

""" # CONTA AS VOGAIS GERAL, NÃO DE CADA PALAVRA
lista = "'Rio de Janeiro', 'Sao Paulo', 'Belo Horizonte', 'Brasilia', 'Salvador', 'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus', 'Belem', 'Goiania'"

def Check_Vow(string, vowels):

    # The term "casefold" has been used to refer to a method of ignoring cases.

    string = string.casefold()

    count = {}.fromkeys(vowels, 0)

    # To count the vowels

    for character in string:

        if character in count:

            count[character] += 1   

    return count

# Driver Code

vowels = 'aeiou'

#string = "Hi, I love eating ice cream and junk food"

string = "'Rio de Janeiro', 'Sao Paulo', 'Belo Horizonte', 'Brasilia', 'Salvador', 'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus', 'Belem', 'Goiania'"


print (Check_Vow(string, vowels))
"""
# PROFESSOR

palavras = ('Rio de Janeiro', 'Sao Paulo', 'Belo Horizonte', 'Brasilia', 'Salvador', 'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus', 'Belem', 'Goiania')

for p in palavras: 
    print (f'\nNa Palavra {p.upper()} temos ', end = '')
    for letra in p :
        if letra.lower() in 'aeiou' :
            print (letra, end = ', ')

palavras = ('Rio de Janeiro', 'Sao Paulo', 'Belo Horizonte', 'Brasilia', 'Salvador', 'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus', 'Belem', 'Goiania')
"""
for p in palavras :
    print (f'\nNa palavra "{p}", temos: ', end = '')
    for letra in p :
        if letra in 'aeiou' :
            print (letra, end = ', ')
            #print ('\n', end = '')
            #print (letra.count('aeiou'), end = '') #quantas letras minúsculas tem na frase
"""
"""
for num in palavras :
    print (f'Que cidade linda {num}', end = '')
    
    print ('',palavras.count('aeiou'))
    #cc = 0
    #print ('',palavras[cc].count('aeiou'))

lista2 = [1,2,3,4,5]

for y in range (0,6) :
    print (f' 3 * {y} = {y*3}')
    y +=1
    #print ('y + 1')
print('')

x = 1
while x in lista2 :
    print (f' 3 * {x} = { 3 * x }')
    x +=1
    #print ('x + 1')

for i in range (6,0, -1) :
    print (i)
print ('FIM')

inicio = int (input ('Início: '))
fim = int (input ('Fim: '))
passo = int (input ('Passo: '))
for c in range (inicio, fim+1, passo) :
    print (f' {inicio} + {passo} = { inicio + passo }')
    passo += 1

for par in range (0, 50+1) :
    if par % 2 != 0 :
        print (par)
print ("Fim 2")
"""

par = 1
while par in (0, 50+1) :
    if par % 2 != 0 :
        print (par)
        par += 1
print ("Fim 3")
