# Crie um programa que leia dois valores e mostre um menu na tela:




from time import sleep

resultado = 0
opcao = 0
while opcao != 5 :
    print ('=' *20, 'menu', '=' * 20)
    primeiro = int (input ('Digite o primeiro número: '))
    segundo = int (input ('Digite o segundo número: '))
    print (''''   [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    opcao = int (input ('Digite a sua opção: '))
    #itens = ('+' , '*' , '>')
    if opcao == 1 :
        resultado = primeiro + segundo
        print ('A soma de {} + {} é: {}' .format (primeiro, segundo, resultado))
    elif opcao == 2:
        resultado = primeiro * segundo
        print ('A multiplicação de {} x {} é: {}' .format (primeiro, segundo, resultado))
    elif opcao == 3:
        if primeiro == segundo :
            maior = 'empatou'
        elif primeiro < segundo :
            maior = segundo
        elif primeiro > segundo :
            maior = primeiro
        print ('o maior entre {} e {} é: {}' .format (primeiro, segundo, maior))
    elif opcao == 4:
        print ('Digite novamente!')
    elif opcao == 5 :
            print ('finalizando...')
    else:
        print ('opção invalida, tente novamente!')
    sleep(1)
       



sleep (2)
print ('Fim do programa, volte sempre!')





