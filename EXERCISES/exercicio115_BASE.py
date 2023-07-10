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

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print ('Houve um ERRO na criação do arquivo!')
    else:
        print ('Arquivo criado com sucesso!')

def lerArquivo (nome) :
    try:
        a = open (nome, 'rt')
    except:
        print ('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        #print (a.read())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print (f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar (arq, nome='desconhecido', idade = 0):
    try:
        a= open(arq, 'at')
    except:
        print('Houve um "ERRO" na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print ('Houve um "ERRO" na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()


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


