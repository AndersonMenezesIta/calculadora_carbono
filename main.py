# Calculadora de Impacto Ambiental para Viagens

def calcular_emissoes(distancia, modo):
    fatores = {
        'carro': 0.12,  # kg CO2 por km (média para carro gasolina)
        'aviao': 0.15,  # kg CO2 por km (média para voo doméstico)
        'trem': 0.04,   # kg CO2 por km (trem elétrico)
        'onibus': 0.08  # kg CO2 por km
    }
    if modo not in fatores:
        return "Modo de transporte inválido."
    return distancia * fatores[modo]

def main():
    print("Calculadora de Impacto Ambiental para Viagens")
    try:
        distancia = float(input("Digite a distância da viagem em km: "))
        modo = input("Escolha o meio de transporte (carro, aviao, trem, onibus): ").lower()
        emissoes = calcular_emissoes(distancia, modo)
        if isinstance(emissoes, str):
            print(emissoes)
        else:
            print(f"Emissões estimadas de CO2: {emissoes:.2f} kg")
    except ValueError:
        print("Por favor, insira um número válido para a distância.")

if __name__ == "__main__":
    main()