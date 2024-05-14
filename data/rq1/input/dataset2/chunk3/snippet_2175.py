#Source: https://stackoverflow.com/questions/60381766/how-do-i-create-a-field-in-my-serializer-to-avoid-a-typeerror-cannot-unpack-no
class Coop(models.Model):
    name = models.CharField(max_length=250, null=False)
    type = models.ForeignKey(CoopType, on_delete=None)
    address = AddressField(on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True, null=False)
    phone = PhoneNumberField(null=True)
    email = models.EmailField(null=True)
    web_site = models.TextField()