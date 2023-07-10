
Variável com vários valores

Tupla 0 1 2 3 
0 sanducihe
1 suco
2 pizza
3 pudim     


print ( lanche [2] ) pizza
print ( lanche [0:2]) sanduiche e suco #ele corta o último elemento
print ( lanche [1:] ) suco pizza pudim #comece no 1 e o : significa vai até o final
print ( lanche [1-] ) pudim #mostra o último elemento
print ( lanche [2] ) 
len(lanche) 4 #quantos elementos tem o lanche

for c in lanche  :     # ele cria uma variavel c automatica mente
    print (c)   # imprime ela com o primeiro elemento do lanche automaticamente
    # no segundo looping ele pega o segundo elemento e assim por diante
    # depois de pegar o último elemento da "Tupla" - "lanche" o "For" acaba automaticamente


AS TUPLAS SÃO IMUTÁVEIS  #não da para trocar elementos dentro dela depois de definida e rodando o programa, para mudar precisa parar de rodar e alterar ela






