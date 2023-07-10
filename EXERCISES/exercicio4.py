n = input ('Digite algo:')

print ('o tipo de primitivo é:', type(n))

print ('Tem numérico?', n.isnumeric())
print ('Tem uma letra?',n.isalpha())
print ('Tem letra e numérico?',n.isalnum())

print ('É somente Espaço?', n.isspace())
print ('Esta em maiúscula?', n.isupper())
print ('Esta em minúscula?', n.islower())
print ('É capitalizada', n.istitle())
 