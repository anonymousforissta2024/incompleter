#Source: https://stackoverflow.com/questions/64882685/typeerror-object-of-type-user-is-not-json-serializable-why-is-this-happening
class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EndUser
        fields = ('id', 'first_name', 'last_name', 'email', 'title', 'user_type', 'packages', 'practice_area',
                  'office_phone', 'level', 'companies', 'country', 'password', 'firm', 'sectors', 'verticals', 'user_ptr')

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.set_password(user.password)
        user.save()