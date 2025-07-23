def multa_localidade(velocidade):
    if velocidade > 50 and velocidade < 90:
        return 60
    elif velocidade >= 90 and velocidade < 120:
        return 120
    elif velocidade >= 120:
        return 320
    else:
        return 0 
    
def multa_fora_da_localidade(velocidade):
    if velocidade > 90 and velocidade < 120:
        return 60
    elif velocidade >= 120:
        return 120
    else:
        return 0

def multa_auto_estrada(velocidade):
    if velocidade > 120 and velocidade <= 150:
        return 60
    elif velocidade > 150 and velocidade <= 175:
        return 120
    elif velocidade > 175:
        return 360
    else:
        return 0
