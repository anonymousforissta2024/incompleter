#Source: https://stackoverflow.com/questions/68362936/python-using-classes-as-default-values-of-another-class-attribute-nameerror
class RateResponse(BaseModel):

    def __init__(self, 
        provider=Provider()
    ):

        self.provider = provider


class Provider(ObjectListModel):

    def __init__(self):

        super(Provider, self).__init__(list=[], listObject=ProviderItem)

    @property
    def providerItems(self):
        return self.list

class ProviderItem(BaseModel):

    def __init__(self,
        code=None,
        notification=Notification(),
        service=Service()
    ):

        self.code = code
        self.notification = notification
        self.service = service