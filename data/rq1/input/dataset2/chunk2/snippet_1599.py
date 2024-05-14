#Source: https://stackoverflow.com/questions/55509211/how-to-resolve-object-of-type-attributeerror-is-not-json-serializable
class Invite_Key(models.Model):
    STATUS_CHOICES = (
        ('valid', 'valid'),
        ('not_valid', 'not_valid'),
        ('banned', 'banned'),
    )

    # Foreign keys
    user_submitter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user_submitter'
    )

    user_receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user_receiver'
    )

    uuid = models.UUIDField(default=generate_ulid_as_uuid, editable=False, unique=True, null=False)
    open_uuid = models.UUIDField(default=uuid1, editable=False, unique=True, null=False)
    reason = models.TextField(validators=[bad_words, bad_words_inline, test_test])

    # Now are choices
    status = models.CharField(max_length=14, choices=STATUS_CHOICES, default="valid")

    # Now below are boolean
    is_taken = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    claim_date = models.DateField(editable=True, null=True, blank=True)
    expire_date = models.DateField(editable=True, null=True, blank=True)

    # Now these are the time stamps
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.uuid)

    # An instance of our object temp used for later
    def __init__(self, *args, **kwargs):
        super(Invite_Key, self).__init__(*args, **kwargs)
        self.temp = ''

    # We can set attributes onSave of our data to the table
    def save(self, *args, **kwargs):
        if not self.id:
            # for expire date
            self.expire_date = datetime.now() + timedelta(days=7)

        super(Invite_Key, self).save(*args, **kwargs)