#Source: https://stackoverflow.com/questions/74286153/typeerror-economico-missing-2-required-positional-arguments-carro-and-con
def entrada_carro():
    carro = []
    for i in range(4):
        carro.append(input("Digite o modelo do carro: "))
    return carro

def entrada_consumo():
    consumo = []
    for i in range(4):
        consumo.append(int(input("Digite o consumo do carro: ")))
    return consumo

def economico(carro, consumo):
    menor = consumo[0]
    for i in range(1,4):
        if consumo[i] < menor:
            menor = consumo[i]
    return carro[consumo.index(menor)]

def main():
    carro = entrada_carro()
    consumo = entrada_consumo()
    print("O carro mais economico é o", economico(carro, consumo))

main()