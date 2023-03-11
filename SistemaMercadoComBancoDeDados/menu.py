import Products as pd
import Clients as cl
import Admin as usr
import resources as sy
from database import userVerify
import database as db
sair = False

def mainMenu():
    a = db.adminCount()
    if not a:
        usr.cadastrarUser()
    print('\nSistema De Mercado\n||' + '=' * 15 + '||\n||  Bem-Vindo(a) ||\n||' + '=' * 15 + '||\n')
    mainMenu = '1-Visualizar estoque\n2-Vender produto\n3-Gerenciar\n4-Mais opções\n0-Sair\n\nEscolha: '

    opcao = int(input(mainMenu))

    if opcao < 0 or opcao > 4:
        print(sy.numError)
    elif opcao == 1:
        pd.visualizarProdutos()
    elif opcao == 2:
        pd.vendaProduto()
    elif opcao == 3:
        user = input('\nUsuário: ')
        password = input('Senha: ')
        if userVerify(user, password):
            gerenciarProdutos()
        else:
            print('\nUsuário ou senha inválida!')
    elif opcao == 4:
        maisMenu()
    elif opcao == 0:
        sai = int(input('\nDeseja encerrar o sistema?\n1-Sim / 2-Não\n\nEscolha: '))
        if sai == 1:
            print('\nSaindo...')
            sair = True
            return sair
        elif sai == 2:
            print(sy.bckMenu)
        else:
            print(sy.numError,sy.bckMenu)


def maisMenu():
    # Menu com algumas funções extras:
    print('\nSistema De Mercado\n')
    print("||" + "=" * 15 + "||\n||  Bem-Vindo(a) ||\n||" + "=" * 15 + "||\n")
    moreMenu = '1-Calcular lucro\n0-Voltar ao menu principal\n\nEscolha: '

    moreMenu = int(input(moreMenu))

    if moreMenu < 0 or moreMenu > 1:
        print(sy.numError)
        maisMenu()
    elif moreMenu == 1:
        sy.lucro()
    elif moreMenu == 0:
        print(sy.bckMenu)


def administrarAdmin():
    # Função para administrar os administradores do sistema:
    print('\nSistema De Mercado\n||' + '=' * 15 + '||\n||  Bem-Vindo(a) ||\n||' + '=' * 15 + '||\n')
    admMenu = int(input('1-Cadastrar novo administrador\n2-Ver administradores\n3-Remover um administrador\n0-Voltar ao menu de gerenciamento\n\nEscolha: '))
    if admMenu > 3 or admMenu < 0:
        print(sy.numError)
        administrarAdmin()
    elif admMenu == 1:
        return usr.cadastrarUser()
    elif admMenu == 2:
        return usr.verUsers()
    elif admMenu == 3:
        return usr.removerUser()
    elif admMenu == 0:
        return gerenciarProdutos()


def gerenciarProdutos():
    # Menu de gerenciamento:
    print('\nSistema De Mercado\n||' + '=' * 15 + '||\n||  Bem-Vindo(a) ||\n||' + '=' * 15 + '||\n')
    mngMenu = int(input('1-Cadastrar produto\n2-Alterar preço\n3-Renomear produto ou fabricante\n4-Remover produto\n5-Lista de vendas\n6-Cadastrar cliente\n7-Visualizar clientes\n8-Gerenciar Administradores\n0-Voltar ao menu principal\n\nEscolha: '))
    if mngMenu > 8 or mngMenu < 0:
        print(sy.numError)
        gerenciarProdutos()
    elif mngMenu == 1:
        pd.cadastrarProduto()
    elif mngMenu == 2:
        pd.alterarPreco()
    elif mngMenu == 3:
        pd.renomearProduto()
    elif mngMenu == 4:
        pd.removeProduto()
    elif mngMenu == 5:
        sy.mostrarVendas()
    elif mngMenu == 6:
        cl.cadastrarCliente()
    elif mngMenu == 7:
        cl.visualizarClientes()
    elif mngMenu == 8:
        administrarAdmin()
    elif mngMenu == 0:
        print(sy.bckMenu)
