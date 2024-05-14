#Source: https://stackoverflow.com/questions/53848930/how-can-i-resolve-this-error-typeerror-nonetype-object-is-not-callable
#This is the model that stores the tender.
class Tender(models.Model):
    tenderCategory = models.ManyToManyField(Category, blank=False)       #this field holds the tender category, e.g. construction, engineering, human resources etc.
    tenderProvince = models.ManyToManyField(Province, blank=False)       #this is the province the tender was advertised from.
    buyersName = models.CharField(max_length=100)   #this is the name of the Buyer e.g. Dept. of Transport, Transnet, Dept of Agriculture etc.
    summary = models.TextField(blank=False)      #this is the tender title as per the Buyer.
    refNum = models.CharField(max_length=100)    #tender ref number as per the Buyer.
    issueDate = models.DateTimeField(blank=True, null=True)     #date the tender was published
    closingDate = models.DateTimeField(default=timezone.now, blank=True, null=True)   #tender closing date
    siteInspectionDate = models.DateTimeField(blank=True, null=True)
    siteInspection = RichTextField(blank=True, null=True)     #site inspection date, if any
    enquiries = RichTextField(blank=True, null=True) #this field stores details of the contact person, for the tender.
    description = RichTextField(blank=True, null=True)   #this is the body of the tender. the tender details are captured here.
    assigned_keywords = models.ManyToManyField(Keywords, blank=True)
    matched = models.BooleanField(default=False, blank=False)
    capture_date = models.DateField(default=timezone.now, blank=False, null=False)
    date_assigned = models.DateField(blank=True, null=True)
    tDocLinks = RichTextField(blank=True)

    def check_if_expired(self):
        if self.closingDate < timezone.now():
            return True
        else:
            return False

    class Meta:
        ordering = ['-closingDate']