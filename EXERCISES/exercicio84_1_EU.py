""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoas = list ()  # ou lista = []
dados = list ()
listamaior = list ()  # ou lista = []
listamenor = []
count = 0
while True :
    dados.append (str(input('Digite um nome: ')))
    #if count == 0 :
    #    listamaior.append = nome
    dados.append (float(input ('Digite o peso: ')))
    pessoas.append(dados[:])
    
    if count == 0 :
            listamaior.append (dados[:])      
            listamenor.append (dados[:])  

    

    #if count == 0 :
    #        listamaior.append = idade
    #c == 0
    #count += 0
    for c in range (1, len(pessoas)) :
        print (f'O C é: {c}')

        #LISTAMENOR
        if (pessoas[c][1]) < (pessoas[c+1][1]) :
            listamenor.clear()
            listamenor.append (dados[:])   
        elif (pessoas[c+1][1]) < (pessoas[c][1]) :
            listamenor.clear()
            listamenor.append (dados[:])       
        elif (pessoas[c+1][1]) == (pessoas[c][1]) :
            listamenor.append (dados[:]) 

        #LISTAMAIOR
        if (pessoas[c][1]) > (pessoas[c+1][1]) :
            listamaior.clear()
            listamaior.append (dados[:])   
        elif (pessoas[c+1][1]) > (pessoas[c][1]) :
            listamaior.clear()
            listamaior.append (dados[:])       
        elif (pessoas[c+1][1]) == (pessoas[c][1]) :
            listamaior.append (dados[:])         

        count += 1

    dados.clear()
    continuar = str (input ('Quer continuar? [S/N]:')).strip().upper()
    if continuar == 'N' :
        break   

    
    print (f'Dados: {dados}')
    print (f'Pessoas: {pessoas}')
    print (f'Lista Menor: {listamenor}')
    print (f'Lista Maior: {listamaior}')

    """
    if (pessoas[c][1]) > (pessoas[c+1][1]) :
        listamaior.clear()
        listamaior.append (pessoas[c])   
    elif (pessoas[c+1][1]) > (pessoas[c][1]) :
        listamaior.clear()
        listamaior.append (pessoas[c])   
    elif (pessoas[c][1]) == (pessoas[c+1][1]) :
        listamaior.append (pessoas[c])   
    """

    """
        if (pessoas[c][1]) <= (pessoas[c+1][1]) :
            listamenor.replace (pessoas[c])
        else:
            listamenor.append (pessoas[c+1])

        if (pessoas[c][1]) >= (pessoas[c+1][1]) :
            listamaior.append (pessoas[c])
        else:
            listamaior.append (pessoas[c+1])
    """

print ('-=' * 25)
print (f'Ao todo vc cadastrou: {count} pessoas')
print (f'Dados: {dados}')
print (f'Pessoas: {pessoas}')
print (f'Lista Menor: {listamenor}')
print (f'Lista Maior: {listamaior}')




