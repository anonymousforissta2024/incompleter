#Source: https://stackoverflow.com/questions/38836795/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.all()
        try:
            for user in users:
                hostname = '%s.%s' % (user.username, settings.NETWORK_DOMAIN)
                stats = Stats.objects.update_or_create(
                    user=user,
                    views=display_pageviews(hostname),
                    visits=display_visits(hostname),
                    unique_visits=display_unique_visits(hostname),)
        except FieldError:
            print ('There was a field error.')