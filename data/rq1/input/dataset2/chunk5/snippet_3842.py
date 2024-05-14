#Source: https://stackoverflow.com/questions/58280786/django-admin-typeerror-int-argument-must-be-a-string-a-bytes-like-object-or
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'model_year', 'mileage', 'status', 'date_added', 'price', 'seller')
    list_filter = ('manufacturer', 'status', 'transmission')
    fieldsets = (
        ('General information', {
            'fields': ('car_images', 'manufacturer', 'model',
            'model_year', 'price', 'vin', 'mileage', 'transmission', 'engine_displacement', 
            'forced_induction', 'drivetrain', 'description', 'id',)
        }),
       ('Availability', {
            'fields': ('status', 'seller')
        }),
    )