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
    print("\nTipo de Estrada")
    print("1 - Localidade")
    print("2 - Fora de Localidade")
    print("3 - Auto Estrada")
    print("0 - Sair")
    
def main():
    loop = True
    while loop == True:
        menu()
        escolha = input("Escolha o tipo de estrada (0 a 3):\n")
        
        if escolha == "1" or escolha == "2" or escolha == "3":
            loop2 = True
            while loop2 == True:
                try:
                    velocidade = int(input("Introduza a velocidade do veículo (km/h):\n"))
                    if velocidade < 0:
                        print("\nErro! Introduza uma velocidade positiva.")
                    else:
                        loop2 = False
                except ValueError:
                    print("Erro! Introduza um valor inteiro para a velocidade!")
            if escolha == "1":
                multa = multa_localidade(velocidade)
                estrada = "numa localidade"
            elif escolha == "2":
                multa = multa_fora_da_localidade(velocidade)
                estrada = "fora da localidade"
            elif escolha == "3":
                multa = multa_auto_estrada(velocidade)
                estrada = "numa auto estrada"
                    
        elif escolha == "0":
            print("\nA encerrar o programa...")
            loop = False
            continue
        else:
            print("\nErro! Opção inválida escolha um número de 0 a 3")
            continue

            
        print(f"\nO veículo seguia a {velocidade} km/h {estrada}.")
        
        if multa == 0:
            print("\nO condutor não tem de pagar multa.")
        else:
            print(f"\nO condutor tem de pagar uma multa de {multa}€\n")


if __name__ == "__main__":
    main()