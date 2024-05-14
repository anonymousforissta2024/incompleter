#Source: https://stackoverflow.com/questions/59848259/typeerror-int-object-is-not-iterable-serializer-django-serializer-for-one-to
class Sector(models.Model):
    sector_name = models.CharField(max_length=255, null=False)
    sector_desc = models.CharField(max_length=1024, null=False)

    def __set__(self):
        return "{} - {}".format(self.sector_name, self.sector_desc)


class TrailCompany(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="sector_id")
    comp_name = models.CharField(max_length=255, null=False)
    comp_desc = models.CharField(max_length=1024, null=False)

    def __set__(self):
        return "{} - {}".format(self.sector, self.comp_name, self.comp_desc)


class Trail(models.Model):
    company = models.ForeignKey(TrailCompany, on_delete=models.CASCADE, related_name="company_id")
    trail_id = models.CharField(max_length=255, null=False)
    tri = models.CharField(max_length=255, null=False)
    exp_pdufa = models.CharField(max_length=255, null=False)

    def __set__(self):
        return "{} - {}".format(self.company, self.exp_pdufa, self.trail_id, self.tri, self.exp_pdufa)