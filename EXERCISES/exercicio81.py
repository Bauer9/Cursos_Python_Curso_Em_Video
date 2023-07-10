""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""



lista = list ()
count = 0
while True :
    lista.append (int (input ("Digite um valor: ")))
    count +=1
    continuar = str (input ('Quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'N' :
        break

print ()
print ('=-' * 20)

print (f'Você digitou: {count} elementos')
lista.sort(reverse = True)
print (lista)
if 5 in lista :
    print ( 'Tem o valor 5 na lista' )
else:
    print ('O valor 5 não está na lista')


