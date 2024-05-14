#Source: https://stackoverflow.com/questions/51946150/django-typeerror-not-supported-between-instances-model-objects
class DeviceModel(models.Model):
    name = models.CharField(max_length=255)
    pirsh = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " - " + self.pirsh

class Device(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=255)


    def __str__(self):
        return self.device_model.name + " - " + self.device_model.pirsh + " - " \
                + self.serial_number

class DeviceTest(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    TEST_OK = '+'
    TEST_ERROR = '-'
    TEST_PENDING = '?'
    TEST_RESULT_CHOICES = (
        (TEST_OK, 'Success'),
        (TEST_ERROR, 'Fail'),
        (TEST_PENDING, 'Not checked'),
    )
    status = models.CharField(max_length=1, choices=TEST_RESULT_CHOICES, default=TEST_PENDING)

    comment = models.TextField(blank=True, default="")
    tester = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        return super(DeviceTest, self).save(*args, **kwargs)

    def __str__(self):
        return  self.device_id.device_model.name + " - " + \
                self.device_id.device_model.pirsh + " - " + \
                self.device_id.serial_number + " - " + \
                str(self.created_at) + " - " + \
                "Result (" + self.status + ")"