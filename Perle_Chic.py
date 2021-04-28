# Project: Perle Chic
# The project is a production and sales price calculator,
# developed for an entrepreneur who owns a beads accessory store.
# Status: In progress


preco_cm1 = 0.0025
preco_cm2 = 0.00068
mdo1 = 3.75
mdo2 = 5.50

# FUNÇÕES PARA PULSEIRAS


def pulseira(cm_pulso, cm_disco):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_disco + 1) * 0.18
    pf = a + b + mdo1
    return '%.2f' % pf


def pulseira2(cm_pulso, cm_micanga):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_micanga + 1) * 0.022
    pf = a + b + mdo1
    return '%.2f' % pf


def pulseira3(cm_pulso, cm_bolinha):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_bolinha + 1) * 0.044
    pf = a + b + mdo1
    return '%.2f' % pf


# FUNÇÕES PARA COLARES


def colar(cm_pescoco, cm_disco):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_disco) * 0.18
    pf = a + b + mdo2
    return '%.2f' % pf


def colar2(cm_pescoco, cm_micanga):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_micanga) * 0.022
    pf = a + b + mdo2
    return '%.2f' % pf


def colar3(cm_pescoco, cm_bolinha):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_bolinha) * 0.044
    pf = a + b + mdo2
    return '%.2f' % pf


while True:
    opcao = input('Digite 1 para pulseira / Digite 2 para colar: ')
    # PULSEIRA
    if opcao == '1':
        opcao_peca = (input('Digite D para disco / Digite M para miçanga / Digite B para bolinha: '))
        # Discos
        if opcao_peca == 'D':
            cm_pulso = float(input('Insira os centímetros da pulseira: '))
            cm_disco = float(input('Insira os centímetros do disco: '))
            print('O custo de produção é: R$', pulseira(cm_pulso, cm_disco))
            print('O custo de venda é: R$', float(pulseira(cm_pulso, cm_disco)) * 3)
            break
        # Miçangas
        elif opcao_peca == 'M':
            cm_pulso = float(input('Insira os centímetros da pulseira: '))
            cm_micanga = float(input('Insira os centímetros da miçanga chinesa: '))
            print('O custo de produção é: R$', pulseira2(cm_pulso, cm_micanga))
            print('O custo de venda é: R$', float(pulseira2(cm_pulso, cm_micanga)) * 3)
            break
        # Bola emborrachada
        elif opcao_peca == 'B':
            cm_pulso = float(input('Insira os centímetros da pulseira: '))
            cm_bolinha = float(input('Insira os centímetros da bolinha: '))
            print('O custo de produção é: R$', pulseira3(cm_pulso, cm_bolinha))
            print('O custo de venda é: R$', float(pulseira3(cm_pulso, cm_bolinha)) * 3)
            break
        else:
            print('Opção inválida. Digite novamente.')
    # COLAR
    elif opcao == '2':
        opcao_peca = (input('Digite D para disco / Digite M para miçanga / Digite B para bolinha: '))
        # Discos
        if opcao_peca == 'D':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            cm_disco = float(input('Insira os centímetros do disco: '))
            print('O custo de produção é: R$', colar(cm_pescoco, cm_disco))
            print('O custo de venda é: R$', float(colar(cm_pescoco, cm_disco)) * 3)
            break
        # Miçangas
        elif opcao_peca == 'M':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            cm_micanga = float(input('Insira os centímetros da miçanga: '))
            print('O custo de produção é: R$', colar2(cm_pescoco, cm_micanga))
            print('O custo de venda é: R$', float(colar2(cm_pescoco, cm_micanga)) * 3)
            break
        # Bola emborrachada
        elif opcao_peca == 'B':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            cm_bolinha = float(input('Insira os centímetros da bolinha: '))
            print('O custo de produção é: R$', colar3(cm_pescoco, cm_bolinha))
            print('O custo de venda é: R$', float(colar3(cm_pescoco, cm_bolinha)) * 3)
            break
        else:
            print('Opção inválida. Digite novamente.')
    # ERRO
    else:
        print('Opção inválida. Digite novamente.')

print('Obrigado por utilizar nosso programa')
