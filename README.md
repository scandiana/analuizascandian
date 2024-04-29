def converter_distancia(valor, unidade_origem, unidade_destino):
    
    fatores = {
        "milhas": 1609.34,
        "polegadas": 0.0254,
        "pes": 0.3048,
        "centimetros": 0.01,
        "metros": 1,
        "quilometros": 1000
    }

    metros = valor*fatores[unidade_origem.lower()]

    valor_convertido = metros / fatores[unidade_destino.lower()]

    return valor_convertido

valor = float(input("Digite o valor a ser convertido: "))
unidade_origem = input("Digite a unidade de origem: ")
unidade_destino = input("Digite a unidade de destino: ")

resultado = converter_distancia(valor, unidade_origem, unidade_destino)
print(f"{valor} {unidade_origem} é igual a {resultado} {unidade_destino}")
