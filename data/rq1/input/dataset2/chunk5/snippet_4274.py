#Source: https://stackoverflow.com/questions/32928255/attributeerror-at-authentication-django-1-8
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=30)
    height = models.FloatField()
    weight = models.FloatField()
    medical_information = models.ForeignKey(MedicalInformation, null=True)
    emergency_contact = models.ForeignKey(EmergencyContact, null=True)
    status = models.ForeignKey(UserStatus, null=True)
    REQUIRED_FIELDS = ['weight', 'height', 'date_of_birth', 'phone_number', 'email', 'first_name', 'last_name']