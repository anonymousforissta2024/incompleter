#Source: https://stackoverflow.com/questions/72492502/nameerror-name-f-is-not-defined
class User(AbstractUser):
    user_pic = models.ImageField(upload_to='img/',default="",null=True, blank=True)
    coins = models.IntegerField(default=10)
    def get_image(self):
        if self.user_pic and hasattr(self.user_pic, 'url'):
            return self.user_pic.url
        else:
            return '/path/to/default/image'
    def give_coins(user, count):
        user.coins = F('coins') + count
        user.save(update_fields=('coins',))
        user.refresh_from_db(fields=('coins',))