#Source: https://stackoverflow.com/questions/65724638/nameerror-name-contact-value-is-not-defined-in-serializers-py
#
# TABLE: CONTACT_METHOD (COME)
#
class ContactMethod(models.Model):
    # attributes:
    contact_value = models.CharField(db_column = 'CONTACT_VALUE', max_length = 255, null=True, blank=True, verbose_name = 'Contact Value')
    effective_period_from = models.DateTimeField(db_column = 'EFFECTIVE_PERIOD_FROM', null=True, blank=True, verbose_name = 'Effective Period From')
    effective_period_to = models.DateTimeField(db_column = 'EFFECTIVE_PERIOD_TO', null=True, blank=True, verbose_name = 'Effective Period To')
    extension_number = models.CharField(db_column = 'EXTENSION_NUMBER', max_length = 255, null=True, blank=True, verbose_name = 'Extension Number')
    notes = models.TextField(db_column = 'NOTES', max_length = 1000, null=True, blank=True, verbose_name = 'Notes')
    created_at = models.DateTimeField(db_column = 'CREATED_AT', verbose_name = 'Created At', editable = False, auto_now_add=True)
    created_by = models.CharField(db_column = 'CREATED_BY', max_length = 255, verbose_name = 'Created By', editable = False)
    updated_at = models.DateTimeField(db_column = 'UPDATED_AT', verbose_name = 'Updated At', editable = False, auto_now=True)
    updated_by = models.CharField(db_column = 'UPDATED_BY', max_length = 255, verbose_name = 'Updated By', editable = False)

    # primary & foreign keys:
    id = models.BigAutoField(db_column = 'ID', primary_key = True)
    # COME_REF_CMTY_FK: ref CONTACT_METHOD_TYPE 
    contact_method_type_id = models.ForeignKey(ContactMethodTypeLv, on_delete = models.DO_NOTHING, db_column = 'CONTACT_METHOD_TYPE_ID', verbose_name = 'Contact Method Type')

    def __str__(self):
        return f'contact_value={self.contact_value} | effective_period_from={self.effective_period_from} | effective_period_to={self.effective_period_to} | extension_number={self.extension_number} | notes={self.notes} | id={self.id} | contact_method_type_id={self.contact_method_type_id} | created_at={self.created_at} | created_by={self.created_by} | updated_at={self.updated_at} | updated_by={self.updated_by}'

    class Meta:
        #abstract = True
        managed = False
        db_table = 'CONTACT_METHOD'
        verbose_name = 'Contact Method'
        verbose_name_plural = 'Contact Methods'
        ordering = (
            'id',
            )