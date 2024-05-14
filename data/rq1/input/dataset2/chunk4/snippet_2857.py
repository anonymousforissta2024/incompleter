#Source: https://stackoverflow.com/questions/69555882/type-error-init-requires-1-positional-argument-yet-2-are-given
class User(AbstractUser):
    is_moderator = models.BooleanField(default = False)
    about = models.TextField(blank = True, null = True)
    notifications = models.ManyToManyField(Notification, related_name = 
    'notifications_user', blank = True)