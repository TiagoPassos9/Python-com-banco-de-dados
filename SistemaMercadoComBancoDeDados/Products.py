import database as db
import resources as sy
import menu as mn
type = 'product'

# Funções
def cadastrarProduto():
    # Função chamada para cadastrar um produto.
    japossui = False
    # Recebe o código do produto.
    codP = int(input('\nCódigo para o produto: '))
    # Procurando se o código de produto já foi cadastrado anteriormente:
    if db.itemVerify(type, codP):
        japossui = True
        print('\nCódigo de produto já existente!')
        choose = int(input('\nProduto não encontrado\n\n1-Tentar novamente\n2-voltar ao menu de gerenciamento\n3-Voltar ao menu principal\n\nEscolha: '))
        if choose == 1:
            return cadastrarProduto()
        elif choose == 2:
            # Volta ao menu de gerenciamento.
            print(sy.bckMenu)
            mn.gerenciarProdutos()
        elif choose == 3:
            # Volta ao menu principal.
            return (sy.bckMenu)
        else:
            # Diz que o número escolhido é inválido e volta ao menu principal.
            return (sy.numError,sy.bckMenu)
    # Pedindo informações do produto se ele ainda não tiver sido cadastrado:
    if (not japossui):
        nomeP = str(input('Nome do produto: ').title())
        fabP = str(input('Nome do fabricante: ').title())
        preco = input('Preço do produto: R$')
        precoP = preco.replace(',', '.')
        qntP = int(input('Quantidade em estoque: '))
        vendaP = 0
        # Cadastrando o produto.
        db.addProduct(type, codP, nomeP, fabP, float(precoP), int(qntP), int(vendaP))
        db.showOne(type, codP, 'all')


# Função para alterar os preços dos produtos:
def alterarPreco():
    productType = 'price'
    idk = 'code'
    japossui = False
    # Alterando o preço:
    codP = int(input('\nCódigo do produto: '))
    if db.itemVerify(type, codP):
        japossui = True
        print('\nPreço atual: ',db.showOne(type, codP, '3'))
        newP = float(input('Digite o novo valor do produto: ').replace(',','.'))
        db.changeProduct(productType, newP, idk, codP)
        return ('\nPreço alterado com sucesso!')
    if (not japossui):
        choose = int(input('\nProduto não encontrado\n\n1-Tentar novamente\n2-voltar ao menu de gerenciamento\n3-Voltar ao menu principal\n\nEscolha: '))
        if choose == 1:
            return alterarPreco()
        elif choose == 2:
            print(sy.bckMenu)
            mn.gerenciarProdutos()
        elif choose == 3:
            return (sy.bckMenu)
        else:
            return (sy.numError,sy.bckMenu)


# Função para realizar a venda dos produtos:
def vendaProduto():
    productType = 'amount'
    idk = 'code'
    japossui = False
    codP = int(input('\nCódigo do produto: '))
    iv = db.itemVerify(type, codP)
    if iv:
        japossui = True
        new = int(input('Quantidade: '))
        if new <= int(db.showOne(type, codP, '4')) and new > 0:
            newA = int(db.showOne(type, codP, '4')) - new
            db.changeProduct(productType, newA, idk, codP)
            print('\nVenda realizada!\n\n')
            comprarMais = int(input('Continuar comprando?\n1-Sim / 2-Não\n\nEscolha: '))
            if comprarMais == 1:
                return vendaProduto()
            elif comprarMais == 2:
                return (sy.bckMenu)
            else:
                return (sy.numError,sy.bckMenu)
        else:
            nameP = db.showOne(type, codP, '1')
            manufP = db.showOne(type, codP, '2')
            amP = db.showOne(type, codP, '4')
            print(f'\nEstoque insuficiente!\nEstoque atual de {nameP} {manufP}: {amP}')
            return vendaProduto()
    if (not japossui):
        choose = int(input('\nProduto não encontrado\n\n1-Tentar novamente\n2- Voltar ao menu principal\n\nEscolha: '))
        if choose == 1:
            return vendaProduto()
        elif choose == 2:
            return (sy.bckMenu)
        else:
            return (sy.numError,sy.bckMenu)


# Função para renomear os produtos ou fabricantes:
def renomearProduto():
    japossui = False
    codP = int(input('\nCódigo do produto para renomear um produto ou fabricante: '))
    iv = db.itemVerify(type, codP)
    if iv:
        chooseOne = int(input('\nDeseja renomear o produto ou o fabricante?\n1-Produto / 2-Fabricante / 3-Sair\n\nEscolha\n'))
        nameP = db.showOne(type, codP, '1')
        manufP = db.showOne(type, codP, '2')
        if chooseOne == 1:
            passou = True
            productType = 'name'
            idk = 'code'
            # Realizando a alteração do nome do produto:
            newName = str(input(f'Novo nome para {nameP} do fabricante {manufP}: '))
            db.changeProduct(productType, newName, idk, codP)
            return ('\nNome alterado com sucesso!')
        elif chooseOne == 2:
            passou = True
            productType = 'manufacturer'
            idk = productType
            # Realizando a alteração do nome do produto:
            newName = str(input(f'Novo nome para o fabricante {manufP}: '))
            allOrOne = int(input(f'Quer alterar {manufP}:\n1-Apenas nesse produto "{nameP}"/ 2-Todos / 3-Sair\n\nEscolha: '))
            if allOrOne == 1:
                idk = 'code'
                db.changeProduct(productType, newName, idk, codP)
            elif allOrOne == 2:
                db.changeProduct(productType, newName, idk, manufP)
            return ('\nFabricante alterado com sucesso!')
        elif chooseOne == 3:
            return(sy.bckMenu)
        else:
            print(sy.numError)
            return renomearProduto()
    if (not japossui):
        choose = int(input('\nProduto não encontrado\n\n1-Tentar novamente\n2-voltar ao menu de gerenciamento\n3-Voltar ao menu principal\n\nEscolha: '))
        if choose == 1:
            return renomearProduto()
        elif choose == 2:
            print(sy.bckMenu)
            mn.gerenciarProdutos()
        elif choose == 3:
            return (sy.bckMenu)
        else:
            return (sy.numError,sy.bckMenu)


# Função para remover um produto:
def removeProduto():
    japossui = False
    codP = int(input('\nCódigo do produto: '))
    iv = db.itemVerify('product', codP)
    if iv:
        japossui = True
        nameP = db.showOne(type, codP, '1')
        manufP = db.showOne(type, codP, '2')
        new = int(input(f'Deseja remover {nameP} {manufP}?\n\n1-Sim / 2-Não\n\nEscolha: '))
        if new == 1:
            db.deleteProduct(type, str(codP))
            return ('\nProduto removido!\n\n')
        elif new == 2:
            return(sy.bckMenu)
        else:
            return(sy.numError,sy.bckMenu)
    if (not japossui):
        choose = int(input('\nProduto não encontrado\n\n1-Tentar novamente\n2-voltar ao menu de gerenciamento\n3-Voltar ao menu principal\n\nEscolha: '))
        if choose == 1:
            return removeProduto()
        elif choose == 2:
            print(sy.bckMenu)
            mn.gerenciarProdutos()
        elif choose == 3:
            return (sy.bckMenu)
        else:
            return (sy.numError,sy.bckMenu)


def visualizarProdutos():
    return db.showAll(type)