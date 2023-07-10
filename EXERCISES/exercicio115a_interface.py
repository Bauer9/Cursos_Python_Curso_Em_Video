def leiaInt (msg) :
    while True:
        try:
            n = int (input(msg))
        except (ValueError, TypeError):  # mais e um erro usar ()
            print('\033[031mERRO: Digite um número válido.\033[m')
        except (KeyboardInterrupt) :
            print('\033[031mERRO: Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha (tam = 42):
    return '-' * tam


def cabecalho (txt) :
    print (linha())
    print (txt)
    print (linha())


def menu (lista) :
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print (f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print (linha())
    opc = leiaInt ('\033[32mSua Opção: \033[m')
    return opc

    """
    print('1 - Ver Pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('-' * 30)
    #return n
    """


