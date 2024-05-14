#Source: https://stackoverflow.com/questions/68362936/python-using-classes-as-default-values-of-another-class-attribute-nameerror
def getInstanceByString(classStr):
    return globals()[classStr]()


class RateResponse(BaseModel):

    def __init__(self, 
        provider=getInstanceByString('Provider')
    ):

        self.provider = provider