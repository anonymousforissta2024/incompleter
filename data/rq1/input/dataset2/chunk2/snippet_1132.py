#Source: https://stackoverflow.com/questions/46482252/attributeerror-resume-object-has-no-attribute-prefetch-related
class Resume(models.Model):
    applicant = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False, help_text="Full Name")

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='educations')
    name = models.CharField(max_length=100, blank=False, null=False, help_text="Name of an institution")