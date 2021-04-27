# Project: Perle Chic
# The project is a production and sales price calculator,
# developed for an entrepreneur who owns a beads accessory store.
# Status: In progress


preco_cm1 = 0.0025
preco_cm2 = 0.00068
mdo1 = 3.75
mdo2 = 5.50


def pulseira(cm_pulso, cm_disco):
    a = preco_cm1 * (cm_pulso + 11)
    b = (cm_disco + 1) * 0.18
    pf = a + b + mdo1
    return '%.2f' % pf


def colar(cm_pescoco, cm_disco):
    a = preco_cm2 * (cm_pescoco + 25)
    b = (cm_disco) * 0.18
    pf = a + b + mdo2
    return '%.2f' % pf


while True:
    opcao = input('Digite 1 para pulseira / Digite 2 para colar: ')
    if opcao == '1':
        cm_pulso = float(input('Insira os centímetros da pulseira: '))
        cm_disco = float(input('Insira os centímetros do disco: '))
        print('O custo de produção é: R$', pulseira(cm_pulso, cm_disco))
        print('O custo de venda é: R$', float(pulseira(cm_pulso, cm_disco)) * 3)
        break
    elif opcao == '2':
        cm_pescoco = float(input('Insira os centímetros do pescoço: '))
        cm_disco = float(input('Insira os centímetros do disco: '))
        print('O custo de produção é: R$', colar(cm_pescoco, cm_disco))
        print('O custo de venda é: R$', float(colar(cm_pescoco, cm_disco)) * 3)
        break
    else:
        print('Valor inexistente.')

print('Obrigado por utilizar nosso programa')
