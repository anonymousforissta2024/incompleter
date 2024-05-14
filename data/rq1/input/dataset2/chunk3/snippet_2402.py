#Source: https://stackoverflow.com/questions/31162350/attributeerror-unsupported-operand-types-for-nonetype-and-nonetype
class Attendancename(models.Model):
    teacher_name = models.ForeignKey(Teachername)
    date = models.DateField('Date')
    intime = models.DateTimeField('IN-TIME')
    outtime = models.DateTimeField('OUT-TIME')

    def hours_calculate(self):
        tdelta = self.outtime - self.intime
        tdelta = float(tdelta)/3600
        return tdelta
    def __str__(self):
        return "%s" %self.teacher_name