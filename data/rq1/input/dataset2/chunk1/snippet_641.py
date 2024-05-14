#Source: https://stackoverflow.com/questions/52675510/attributeerror-settings-object-has-no-attribute-auth-user-model-value-after
class User(AbstractUser):

    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    objects = NewUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    class Meta(AbstractUser.Meta):
        swappable = 'stack.User'