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
    nota2 = float (input ('Digite a primeira nota: '))
    alunos.append ([nota1, nota2])
    media = (nota1 + nota2)  / 2
    alunos.append (media)
    boletim.append (alunos[:])
    alunos.clear ()
    print (boletim)
    pergunta = str (input ('Quer continuar? [S/N]')).strip().upper()
    if pergunta == 'N' :
        break 

    #print (f'Boletim  0: {boletim[0]}')
    c = 0
    #print (f'Imprimir Boletim C: {boletim[c]}')

       
print ('-=' *30)
print (f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print ('-' *26)
for i, a in enumerate (boletim) :
    print (f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True :
    print ('-' * 35)
    opc = int (input ('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999 :
        print ('FINALIZANDO...')
        break   
    if opc <= len(boletim) - 1 :
        print (f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')  

print ('<<< VOLTE SEMPRE >>>')   

