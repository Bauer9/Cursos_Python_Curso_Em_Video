"""
Faça um mini-sistema que utilize a ajuda interativa do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM' ('END'), o programa será fechado. Importante: Use cores.
"""
from time import sleep

c = ('\033[m',          # 0 - sem cores # padrao ansy de cores, padrão ansy
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 1 - verde
     '\033[0;30;43m',   # 1 - amarelo
     '\033[0;30;44m',   # 1 - azul
     '\033[0;30;45m',   # 1 - roxo
     '\033[7;30m'        # 1 - branco
     ); 

def ajuda (msg) :
    titulo (f'Acessando o manual do comando \'{msg}\'', 4)
    print (c[6], end = '')
    help (msg)
    print (c[0], end = '')
    sleep (2)
    
def titulo (msg1, cor = 0) :
    tam = len (msg1) + 4
    print (c[cor], end = '')
    print ('~' * tam)
    print (f'  {msg1}')
    print ('~' * tam)
    print (c[0], end = '')
    sleep (1)

# PROGRAMA PRINCIPAL
comando = ''
while True :
    titulo ('SISTEMA DE AJUDA PyHELP', 2)
    comando = str (input ("Função ou Biblioteca > "))#.strip()#.upper()
    if comando.upper() == 'FIM' :
        break
    else:
        ajuda(comando)

titulo ('ATÉ LOGO!', 1)

#print (ajuda)
#print ('FIM')

