#Source: https://stackoverflow.com/questions/74286153/typeerror-economico-missing-2-required-positional-arguments-carro-and-con
def main():
    carro = entrada_carro()
    consumo = entrada_consumo()
    print("O carro mais economico é o", economico(carro, consumo))

main()