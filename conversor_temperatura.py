# Função para converter a temperatura
def converter_temperatura(valor, origem, destino):
    # Converte a temperatura de origem para Celsius
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5/9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        return "Unidade de origem inválida."

    # Converte de Celsius para a unidade de destino
    if destino == "C":
        return celsius
    elif destino == "F":
        return celsius * 9/5 + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return "Unidade de destino inválida."

# Entrada do usuário
valor = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

# Conversão e saída
resultado = converter_temperatura(valor, origem, destino)

# Verifica se houve erro
if isinstance(resultado, str):
    print(resultado)
else:
    print(f"{valor}°{origem} = {resultado:.2f}°{destino}")
