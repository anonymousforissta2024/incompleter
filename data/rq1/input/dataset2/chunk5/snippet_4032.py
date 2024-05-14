#Source: https://stackoverflow.com/questions/62971435/learning-inheritance-typeerror-init-takes-3-positional-arguments-but-5
class BasicToken:

    asset_class = "Crypto-Currency"

    def __init__(self, symbol):
        self.symbol = symbol


class StableCoin(BasicToken):
    def __init__(self, color, supply):
        self.color = color
        self.supply = supply

icon = BasicToken('icx')
icxStable = StableCoin('DMM', ['Blue', 'White'])

print('Icon Symbol: '+ icon.symbol)
print('IcxStable Symbol: '+ icxStable.symbol)