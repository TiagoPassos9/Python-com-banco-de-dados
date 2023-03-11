numError = '\nO número digitado não corresponde a nenhuma das alternativas.\n'
bckMenu = '\nVoltando ao menu...\n'
manutencao = '\nVolte novamente mais tarde, página em manutenção...\n'
traco = '-' * 14

# Refazer
def mostrarVendas():
    return print(manutencao)

def lucro():
    nome = str(input('\nNome do produto: '))
    qnt = int(input('Quantidade comprada: '))
    pagoP = float(input('Preço total pago: R$'))
    porcentagem = int(input('Qual será a porcentagem de lucro?\n'))

    pago = pagoP / qnt
    porcentagemD = porcentagem / 100
    totalPorcentagem = pago * porcentagemD
    total = pago + totalPorcentagem
    
    return print(f'Ao vender {nome} com {porcentagem}% de lucro, equivalente a R${totalPorcentagem:.2f} por produto vendido com o valor de R${total:.2f}')
