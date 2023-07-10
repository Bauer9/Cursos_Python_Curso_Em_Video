"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""
"""
def contador3 (*num) :
    tam = len(num)
    print (f'Recebi os valores {num} que não ao todo {tam} números')
""" 
"""
notasDic = list ()

while True :
    n = int (input ('Digite uma nota: '))
    notasDic.append(n)
    while True :
        pergunta = str (input ('Quer continuar? [S/N]: ')).strip().upper()
        if 'SN' != pergunta :
            print ('INVALIDO, Digite S ou N')
        if pergunta in 'N' :
            break
        if 'S' in pergunta :
            break
    if pergunta in 'N' :
        break 
"""

"""
print (f'Sua nota é {n} ')
print (f'Sua lista é {notasDic} ')

print ('FIm')
"""


#resp = notas (5.5, 9.5, 10, 6.5, sit = True)


def notas (*n, sit = False) :

    #>> Função
    #:- Quantidade de notas
    #:- A maior nota
    #:- A menor nota
    #:- A média da turma
    #:- A situação (opcional)


    r = dict ()
    r['total'] = len (n)
    r['maior'] = max (n)
    r['menor'] = min (n)
    r['media'] = sum (n)/len(n)
    if sit :
        if r ['media'] >= 9 :
            r ['situacao'] = 'ÓTIMA'
        elif r ['media'] >= 7 and r ['media'] < 9:
            r ['situacao'] = 'BOA'
        elif r ['media'] >= 5 :
            r ['situacao'] = 'RAZOÁVEL'    
        else: 
            r ['situacao'] = 'RUIM'        
    
    return r
    
resp = notas (5.5, 9.5, 10, 6.5, sit = True)
#resp = notas (5.5, 9.5, 10, 6.5)
print (resp)
help (notas)


def func1 (*num,) :
    dict2 = dict ()
    dict2['total'] = len (num)
    dict2['maior'] = max (num)
    dict2['menor'] = min (num)
    dict2['media'] = sum (num)/len(num)
    return dict2


resp1 = func1 (3.0, 7.0, 2.5, 1.0, 9.5)

#print (dict2)
print (resp1)


