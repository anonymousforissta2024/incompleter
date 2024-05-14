#Source: https://stackoverflow.com/questions/58784123/one-to-one-relationship-how-to-fix-got-attributeerror-when-attempting-to-get-a
class MyUser(AbstractBaseUser):
    username = models.CharField(
        max_length=300,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email address'
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

class Profile (models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE) 
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures') #blank - true
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'