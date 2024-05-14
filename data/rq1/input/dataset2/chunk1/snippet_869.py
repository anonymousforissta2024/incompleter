#Source: https://stackoverflow.com/questions/56637422/why-is-user-query-triggering-typeerror
class CustomUser(AbstractUser):
    username = models.CharField(max_length=11, blank=True, default= 
     'newUser', verbose_name="User Group")
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager

    # add additional fields in here
    display_name = models.SlugField(max_length=50, unique=True)
    phone = models.CharField(max_length=14, blank=True, help_text="XXX-XXX-XXXX")

    def __str__(self):
        return self.display_name