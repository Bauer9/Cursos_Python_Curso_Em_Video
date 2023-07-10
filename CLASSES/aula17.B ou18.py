teste = list ()
teste.append('Gustavo')
teste.append(40)
print (teste)
galera = list ()
#galera.append(teste) # as duas ficam ligadas
galera.append(teste[:]) # cria uma cópia
teste[0] = 'Maria'
teste[1] = 22
#galera.append(teste)
galera.append(teste[:])
print (galera)

galera1 = [[ 'Pedro', 25], [ 'Maria', 19], [ 'João', 32], [ 'Joaquim', 36]]
for p in galera1 :
    #print (p[0], end = ', ')
    #print (p[1], end = ', ')
    print (f'{p[0]} tem {p[1]} anos de idade.')

galera2 = list ()
dado = list ()
totalmaior = totalmenor = 0 
for c in range (0, 3) :
    dado.append (str(input('Nome: ')))
    dado.append (int(input('Idade: ')))    
    galera2.append (dado[:]) #[:] copia a lista, o Clear apaga o Dados e não a galera2
    dado.clear()

print (galera2)

for p in galera2 :
    if p[1] >= 21:
        print (f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print (f'{p[0]} é menor de idade.')
        totalmenor += 1

print (f'Temos tantos {totalmaior} maiores e {totalmenor} menores de idade.')
