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
    
def menu():
    print("Tipo de Estrada")
    print("1 - Localidade")
    print("2 - Fora de Localidade")
    print("3 - Auto Estrada")
    print("0 - Sair")
    
def main():
    loop = True
    while loop == True:
        menu()
        escolha = input("Escolha o tipo de estrada (0 a 3):\n")
        
        if escolha == "0":
            print("A encerrar o programa...")
            loop = False
            continue
        velocidade = int(input("Introduza a velocidade do veículo (km/h)"))
        
        if escolha == "1":
            multa = multa_localidade(velocidade)
            estrada = "Numa Localidade"
        elif escolha == "2":
            multa = multa_fora_da_localidade(velocidade)
            estrada = "Fora da Localidade"
        elif escolha == "3":
            multa = multa_auto_estrada(velocidade)
            estrada = "Numa Auto Estrada"
        else:
            print("Erro! Opção inválida escolha um número de 0 a 3")
            continue
            
        print(f"O veículo seguia a {velocidade} km/h {estrada}.")
        
        if multa == 0:
            print("O condutor não tem de pagar multa.")
        else:
            print(f"O condutor tem de pagar uma multa de {multa}€")


if __name__ == "__main__":
    main()