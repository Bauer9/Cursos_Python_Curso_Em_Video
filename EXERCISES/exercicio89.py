# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = list ()
alunos = list ()
count = 0
media = 0
while True :
    nome = str (input ('Digite o nome do aluno: '))
    alunos.append (nome)
    nota1 = float (input ('Digite a primeira nota: '))
    alunos.append (nota1)
    nota2 = float (input ('Digite a primeira nota: '))
    alunos.append (nota2)
    media = (nota1 + nota2)  / 2
    alunos.append (media)
    boletim.append (alunos[:])
    alunos.clear ()
    print (boletim)
    pergunta = str (input ('Quer continuar? [S/N]')).strip().upper()


    #print (f'Boletim  0: {boletim[0]}')
    c = 0
    #print (f'Imprimir Boletim C: {boletim[c]}')

    while pergunta == 'N' :
    #if pergunta == 'N'  :
        
        print ('-=' *30)
        print ('No.     NOME        MÉDIA ')
        
        for c in range (0, len(boletim)) :
            #print (f'Boletim 0: {boletim[0]}')
            #print (f'Boletim aluno {c}: {boletim[c]}')
            print (f'{c}         {boletim[c][0]}          média {(boletim[c][1]+boletim[c][2]) / 2}')
            c += 1
        
        print ('-'  * 35)
        aluno = int (input ('Mostrar notas de qual aluno? (999 interrompe)'))

        for c, aluno in enumerate (boletim) :
            if c == 0 :
                print (f'Aluno 0 as notas são: {boletim[c][1]} e {boletim[c][2]}')
            #elif c == 1 :
            #    print (f'Aluno 0 as notas são: {boletim[c]+1[1]} e {boletim[c+1][2]}')
            #elif c == 2 :
            #    print (f'Aluno 0 as notas são: {boletim[c]+2[1]} e {boletim[c+2][2]}')
            #print ('-=' *30)

        
        if aluno <= len(boletim) -1 :
            print ()
            print (f'Boletim nome: {boletim[aluno][0]}', end = '')
            #print (f'Boletim: {(boletim[aluno][1])}, {(boletim[aluno][2])}')
            #print (f'Boletim C: {boletim[c]}')


        #print (f'Aluno 0 as notas são: {boletim[0][1]} e {boletim[0][2]}')


        #if aluno == '0' : 
        #    
    if pergunta == 999 :
        break 

    #print (f'Alunos {alunos}')   
    #print ( f'Boletim {boletim}')
  