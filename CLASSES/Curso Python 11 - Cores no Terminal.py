
# style;text;back (cor de fundo)
# style = 0 (none, sem estilo), 1 (bold) ,4 (underline) e 7 (negative)

# STYLE
# 0 (none, sem estilo)
# 1 (bold)
# 4 (underline)
# 7 (negative)

# \033[style; text ;back m]
# \033[0 ;33 ;44 m]

# TEXT - de 30 a 37
# 30  white
# 31  red
# 32  green
# 33  yellow
# 34  blue
# 35  purple
# 36  cian - white blue
# 37  grey
 
#BACK - de 40 a 47
# 40  white
# 41  red
# 42  green
# 43  yellow
# 44  blue
# 45  purple
# 46  cian - white blue
# 47  grey
 

# \033[0;33;44m]


print ('\033[4;31;43m text \033[m' )

print ('\033[7;30;44m text \033[m' )

print ('\033[1;30;43m text \033[m' )


a = 3 
b = 5
print ('Os valores são \033[32m{}\033[m e \033[31m{}' .format(a, b) )

nome = 'Felipe'
cores = {'limpa' : '\033[m', 
        'azul' : '\033[34m' , 
        'amarelo' : '\033[33m' , 
        'pretoebranco' : '\033[30;1;41m', 
        'brancoepreto' : '\033[31;7;39m' 


        }
print ('Olá! muito prazer em te conhecer {}{}{}!!'.format ('\033[4;34m' , nome, '\033[m' ))


print ('Muitas cores 1 {}{}{}!!'.format (cores['pretoebranco'] , nome, cores['limpa'] ))

print ('Muitas cores 2 {}{}{}!!'.format (cores['brancoepreto'] , nome, cores['limpa'] ))



