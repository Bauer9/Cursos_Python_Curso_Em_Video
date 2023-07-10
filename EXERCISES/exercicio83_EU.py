# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = list ()
num = str (input ('Digite uma expressão: '))
#num = str (input ('Digite uma expressão: '))
#expressao.append (num)
countA = 0
countB = 0

for simb in num :
#while True :
    if simb == '(' :
        expressao.append ('(')
        countA += 1
        #print (countA)
    elif simb == ')' :
        expressao.append (')')
        countB += 1
        #print (countB)
        
        """
        if countA + countB  % 2 == 0 :
            print ('Expressão correta!4')     
            break
        if countA % 2 == 0 and countB % 2 == 0 :
            print ('Expressão correta!5')   
        if countB % 2 == 0 :
            print ('Expressão correta!2')
            break
        #elif countA % 2 == 0  :
        #    print ('Expressão correta!3')
        #    break
        else : 
            print ('Incorrreto!')
            break
        """
    #if countB + countA == 2:
    #    print ('Expressão correta!1')
    #    break
    
    
            
        
        #if countA+countB == 2 :
        #   print ('Expressão correta!')

print (f'CountA tem {countA}')
print (f'CountB tem {countB}')
print ('FIM')
print (expressao)


"""
if countA % 2 == 0 and countB % 2 == 0 :
    print ('Expressão correta!')
else:
    print ('Expressão incorreta!')
"""



#if '()' in expressao % 2 == 0 :
#   print ('Expressão correta!')


#res1 = expressao.find ('(')
#res2 = expressao.find (')')
#res3 = expressao.find ('(') + expressao.find (')')
#print (f'res1 é {res1}') 
#print (f'res2 é {res2}') 
#print (f'res3 é {res3}') 





"""
for v  in enumerate (expressao) :
    if v == ('(') :
        print (f'{i}..., ', end = '')
"""


"""
if res1 % 2 == 0 :
    if res2 % 2 == 0 :
        print ('Expressão correta!')
    else:
        print ('Expressão incorreta!')
"""
"""   
if res3 % 2 == 0 :  
    print ('Expressão correta!')
else:
    print ('Expressão incorreta!')
"""
# frase.find('deo') quantas vezes encontrou o 'deo', mostra em que momento começou - casa 11

