#Source: https://stackoverflow.com/questions/50591953/typeerror-not-supported-between-instances-of-printer-and-int
products = {

    "A": [100, "cola"],
    "B": [100, "drink0"]

}


def coinCounter():
    print("Bitte Münzen einwerfen! / Betrag eingeben!")

    credits = int(input("Betrag: "))


def product():
    print("Bitte Produkt wählen!")

    choosedProduct = input("Produkt: ").capitalize()

    if choosedProduct in products and credits >= products[choosedProduct][0]:
        output = True
    elif choosedProduct not in products:
        print("Das Produkt existiernt nicht.")
    elif products[choosedProduct][0] >= credits:
        print("Du hast nicht genug Geld eingeworfen")

    def moneyBack(moneyBack):
        moneyBack = credits - products[choosedProduct][0]
        print("Zurück: ", moneyBack)


    def output(output, choosedProduct):
        if output == True:
            print("Das Produkt", choosedProduct[1], "wird ausgegeben...")
            output = False

    output()
    moneyBack()



def main():
    coinCounter()
    product()

main()