#Source: https://stackoverflow.com/questions/50107541/hybrid-property-raises-a-typeerror-in-if-else
@hybrid_property
def conversion_number(self):
    return 'P0{}'.format(self.id) if self.id < 10 else 'P{}'.format(self.id)