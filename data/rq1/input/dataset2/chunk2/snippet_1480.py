#Source: https://stackoverflow.com/questions/51141597/django-typeerror-got-multiple-values-for-argument
class LocationManager(models.Manager):
    def exist(city, state):
        if self.queryset.get(city=city, state=state):
            return True
        return False

    def create_new(self, ip_address, city_data):
        location = self.model()
        if ip_address is not None:
            if city_data:
                city = city_data['city']
                state = city_data['region']
                if not self.exist(city=city, state=state):
                    location.city_data = city_data
                    location.city = city
                    location.state = state
                    location.country = city_data['country_name']
                    location.latitude = city_data['latitude']
                    location.longitude = city_data['longitude']
                    location.save()
                    return location
                else:
                    return Location.objects.get(city=city, state=state)

class Location(models.Model):
    city_data   = models.TextField(null=True, blank=True)
    city        = models.CharField(max_length=120, null=True, blank=True)
    state       = models.CharField(max_length=2, null=True, blank=True)
    country     = models.CharField(max_length=20, null=True, blank=True)
    latitude    = models.FloatField()
    longitude   = models.FloatField()

    objects = LocationManager()

    def __str__(self):
        return '{}, {}'.format(self.city, self.state)