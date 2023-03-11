import database as db
import resources as sy
import menu as mn
type = 'users'

def cadastrarUser():
    print('\nCadastro de Usuário\n')
    japossui = False
    # Recebe o usuário do administrador.
    while True:
        user = input('\nUsuário: ')
        if len(user) <= 3:
            print('Usuário precisa ter pelomenos 4 carácters!')
        else:
            break
    # Procurando se o usuario já foi cadastrado anteriormente:
    if db.itemVerify(type, user):
        japossui = True
        print('\nUsuário já existente!')
        choose = int(input('1-Tentar novamente / 2-voltar ao menu\n\nEscolha: '))
        if choose == 1:
            # Chama novamente a função.
            return cadastrarUser()
        elif choose == 2:
            print(sy.bckMenu)
            # Volta ao menu de gerenciamento.
            return mn.gerenciarProdutos()
        else:
            # Diz que o número escolhido é inválido e volta ao menu de gerenciamento.
            print(sy.numError,sy.bckMenu)
            return mn.gerenciarProdutos()
    # Pedindo informações do cliente se ele ainda não tiver sido cadastrado:
    if (not japossui):
        while True:
            password = str(input('Senha: '))
            passwordConfirmation = str(input('Digite novamente: '))
            if len(password) < 4:
                print('A senha precisa ter pelomenos 4 carácters!')
            elif password == passwordConfirmation:
                #dando um código
                codA = db.adminCountNumbers()
                # Cadastrando o usuário.
                db.addProduct(type, codA, user, password)
                print('\nusuário cadastrado!\n')
                return mn.gerenciarProdutos()
            else:
                print('as senhas não são iguais')


def removerUser():
    japossui = False
    print('\nVerificação')
    user = input('\nAdmin: ')
    password = input('Senha: ')
    if db.userVerify(user, password):
        japossui = True
        name = input('Usuário a ser removido: ')
        db.showOne(type, name, '1')
        if db.itemVerify(type, name):
            new = int(input(f'Deseja remover o admin {name}?\n\n1-Sim / 2-Não\n\nEscolha: '))
            if new == 1:
                code = db.getCode(type, name)
                db.deleteProduct(type, str(code))
                return (print('\nUsuário removido!\n\n'))
            elif new == 2:
                return(sy.bckMenu)
            else:
                return(sy.numError,sy.bckMenu)
    if (not japossui):
        choose = int(input('\nUsuário não encontrado\n\n1-Tentar novamente / 2-voltar ao menu\n\nEscolha: '))
        if choose == 1:
            return removerUser()
        elif choose == 2:
            return(sy.bckMenu)
        else:
            return(sy.numError,sy.bckMenu)


def verUsers():
    db.showAll(type)
    mn.administrarAdmin()
