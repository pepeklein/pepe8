# Project: Perle Chic
# The project is a production and sales price calculator,
# developed for an entrepreneur who owns a beads accessory store.
# Status: In progress (Beta Version)


preco_cm1 = 0.0025  # Preço centímetro do silicone
preco_cm2 = 0.00068  # Preço centímetro do nylon
mdo1 = 3.75  # Preço mão de obra das pulseiras
mdo2 = 5.50  # Preço mão de obra dos colares


# PULSEIRAS

# DOC1: cm_pulso + 11 = centímetros de sobra do silicone para amarração
# DOC2: cm_micanga + 1 = centímetro de folga no pulso


# Disco
def pulseira(cm_pulso, cm_disco):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_disco + 1) * 0.18
    pf = a + b + mdo1
    return '%.2f' % pf


# Miçanga
def pulseira2(cm_pulso, cm_micanga):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_micanga + 1) * 0.022
    pf = a + b + mdo1
    return '%.2f' % pf


# Bola emborrachada
def pulseira3(cm_pulso, cm_bolinha):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_bolinha + 1) * 0.044
    pf = a + b + mdo1
    return '%.2f' % pf


# Bola prateada grande
def pulseira4(cm_pulso, cm_prateada):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_prateada + 1) * 0.41
    pf = a + b + mdo1
    return '%.2f' % pf


# Miçanga Jablonex
def pulseira5(cm_pulso, cm_micangaj):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_micangaj + 1) * 0.05
    pf = a + b + mdo1
    return '%.2f' % pf


# COLARES

# DOC1: cm_pescoco + 25 = centímetros de sobra de nylon


# Disco
def colar(cm_pescoco, cm_disco):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_disco) * 0.18
    pf = a + b + mdo2
    return '%.2f' % pf


# Miçanga chines
def colar2(cm_pescoco, cm_micanga):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_micanga) * 0.022
    pf = a + b + mdo2
    return '%.2f' % pf


# Bola emborrachada
def colar3(cm_pescoco, cm_bolinha):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_bolinha) * 0.044
    pf = a + b + mdo2
    return '%.2f' % pf


# Bola prateada mini
def colar4(cm_pescoco, cm_miniprata):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_miniprata) * 0.011
    pf = a + b + mdo2
    return '%.2f' % pf


# Nylon + pingente
def colar5(cm_pescoco):
    a = preco_cm2 * (cm_pescoco + 25)
    pf = a + mdo2
    return '%.2f' % pf


# Miçanga jablonex
def colar6(cm_pescoco, cm_micangaj):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_micangaj) * 0.05
    pf = a + b + mdo2
    return '%.2f' % pf


while True:
    opcao = input('Digite 1 para pulseira / Digite 2 para colar: ')
    # PULSEIRA
    if opcao == '1':
        opcao_peca = (input('Digite D para disco / Digite M para miçanga chinesa / Digite B para bola emborrachada / Digite P para bola prateada grande / Digite J para jablonex: '))
        # Discos
        if opcao_peca == 'D' or 'd':
            cm_pulso = float(input('Insira os centímetros do pulso: '))
            cm_disco = float(input('Insira os centímetros do disco: '))
            print('O custo de produção é: R$', pulseira(cm_pulso, cm_disco))
            print('O custo de venda é: R$', float(pulseira(cm_pulso, cm_disco)) * 3)
            break
        # Miçangas
        elif opcao_peca == 'M' or 'm':
            cm_pulso = float(input('Insira os centímetros do pulso: '))
            cm_micanga = float(input('Insira os centímetros da miçanga chinesa: '))
            print('O custo de produção é: R$', pulseira2(cm_pulso, cm_micanga))
            print('O custo de venda é: R$', float(pulseira2(cm_pulso, cm_micanga)) * 3)
            break
        # Bola emborrachada
        elif opcao_peca == 'B' or 'b':
            cm_pulso = float(input('Insira os centímetros do pulso: '))
            cm_bolinha = float(input('Insira os centímetros da bola emborrachada: '))
            print('O custo de produção é: R$', pulseira3(cm_pulso, cm_bolinha))
            print('O custo de venda é: R$', float(pulseira3(cm_pulso, cm_bolinha)) * 3)
            break
        # Bola prateada
        elif opcao_peca == 'P' or 'p':
            cm_pulso = float(input('Insira os centímetros do pulso: '))
            cm_prateada = float(input('Insira os centímetros da bola prateada grande: '))
            print('O custo de produção é: R$', pulseira4(cm_pulso, cm_prateada))
            print('O custo de venda é: R$', float(pulseira4(cm_pulso, cm_prateada)) * 3)
            break
        # Jablonex
        elif opcao_peca == 'J' or 'j':
            cm_pulso = float(input('Insira os centímetros do pulso: '))
            cm_micangaj = float(input('Insira os centímetros da miçanga jablonex: '))
            print('O custo de produção é: R$', pulseira5(cm_pulso, cm_micangaj))
            print('O custo de venda é: R$', float(pulseira5(cm_pulso, cm_micangaj)) * 3)
            break
        else:
            print('Opção inválida. Digite novamente.')
    # COLAR
    elif opcao == '2':
        opcao_peca = (input('Digite D para disco / Digite M para miçanga / Digite B para bola emborrachada / Digite MP para bola prateada mini / Digite J para jablonex: '))
        # Discos
        if opcao_peca == 'D' or 'd':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            cm_disco = float(input('Insira os centímetros do disco: '))
            print('O custo de produção é: R$', colar(cm_pescoco, cm_disco))
            print('O custo de venda é: R$', float(colar(cm_pescoco, cm_disco)) * 3)
            break
        # Miçangas
        elif opcao_peca == 'M' or 'm':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            cm_micanga = float(input('Insira os centímetros da miçanga: '))
            print('O custo de produção é: R$', colar2(cm_pescoco, cm_micanga))
            print('O custo de venda é: R$', float(colar2(cm_pescoco, cm_micanga)) * 3)
            break
        # Bola emborrachada
        elif opcao_peca == 'B' or 'b':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            cm_bolinha = float(input('Insira os centímetros da bola emborrachada: '))
            print('O custo de produção é: R$', colar3(cm_pescoco, cm_bolinha))
            print('O custo de venda é: R$', float(colar3(cm_pescoco, cm_bolinha)) * 3)
            break
        # Mini prata
        elif opcao_peca == 'MP' or 'mp':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            cm_miniprata = float(input('Insira os centímetros da bola prateada mini: '))
            print('O custo de produção é: R$', colar4(cm_pescoco, cm_miniprata))
            print('O custo de produção é: R$', float(colar4(cm_pescoco, cm_miniprata)) * 3)
        # Nylon + Pingente
        elif opcao_peca == 'NP' or 'np':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            print('O custo de produção é: R$', colar5(cm_pescoco))
            print('O custo de produção é: R$', float(colar5(cm_pescoco)) * 3)
        # Miçanga jablonex
        elif opcao_peca == 'J' or 'j':
            cm_pescoco = float(input('Insira os centímetros do pescoço: '))
            cm_micangaj = float(input('Insira os centímetros da miçanga jablonex: '))
            print('O custo de produção é: R$', colar6(cm_pescoco, cm_micangaj))
            print('O custo de produção é: R$', float(colar6(cm_pescoco, cm_micangaj)) * 3)
        else:
            print('Opção inválida. Digite novamente.')
    # ERRO
    else:
        print('Opção inválida. Digite novamente.')

print('Obrigado por utilizar nosso programa')
