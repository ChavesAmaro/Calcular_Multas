def multa_localidade(velocidade)
    if velocidade > 50 and velocidade < 90:
        return 60
    elif velocidade >= 90 and velocidade < 120:
        return 120
    elif velocidade >= 120:
        return 320
    else:
        return 0 