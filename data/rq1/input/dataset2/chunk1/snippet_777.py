#Source: https://stackoverflow.com/questions/58575057/update-throwing-typeerror-serializer-update-got-an-unexpected-keyword-argum
class SMSMessages(models.Model):
    sms_number_to = models.CharField(max_length=14)
    sms_content = models.CharField(max_length=160)
    sending_user = models.ForeignKey("SMSUser", on_delete=models.PROTECT, related_name="user_that_sent")
    sent_date = models.DateTimeField(auto_now=True)
    delivery_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "SMSMessages"

    def __str__(self):
        return str(self.sending_user)