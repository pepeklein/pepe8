# Project: Perle Chic
# The project is a production and sales price calculator,
# developed for an entrepreneur who owns a beads accessory store.
# Status: In progress


preco_cm = 0.0025
mdo1 = 3.70
mdo2 = 4.10


def pulseira(cm_pulso, cm_disco):
    a = preco_cm * cm_pulso
    b = (cm_disco + 1) * 0.18
    pf = a + b + mdo1
    return '%.2f' % pf


def colar(cm_pescoco, cm_disco):
    a = preco_cm * cm_pescoco
    b = (cm_disco) * 0.18
    pf = a + b + mdo2
    return '%.2f' % pf


opcao = input('Se trata de uma pulseira ou de um colar? ')
if opcao == 'pulseira':
    cm_pulso = float(input('Insira os centímetros da pulseira: '))
    cm_disco = float(input('Insira os centímetros do disco: '))
    print(pulseira(cm_pulso, cm_disco))
elif opcao == 'colar':
    cm_pescoco = float(input('Insira os centímetros do pescoço: '))
    cm_disco = float(input('Insira os centímetros do disco: '))
    print(colar(cm_pescoco, cm_disco))
