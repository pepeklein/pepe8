import time

preco_cm = 0.0025
mdo1 = 3.70
mdo2 = 4.10


def pulseira(cm_pulso, cm_disco):
    a = preco_cm * cm_pulso
    b = (cm_disco + 1) * 0.18
    pf = a + b
    return pf + mdo1


def colar(cm_pescoco, cm_disco):
    a = preco_cm * cm_pescoco
    b = (cm_disco) * 0.18
    pf = a + b
    return pf + mdo2


time.sleep(600)
