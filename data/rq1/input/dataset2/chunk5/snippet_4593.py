#Source: https://stackoverflow.com/questions/63704863/attributeerror-at-str-object-has-no-attribute-get-in-danjo
first_name = models.CharField(max_length = 20) 
last_name = models.CharField(max_length = 20)
password = models.CharField(max_length = 12)
confirm_password = models.CharField(max_length = 12)
phone_number = models.CharField(max_length = 10)
gender = models.CharField(max_length = 6)
city = models.CharField(max_length = 20)

def __str__(self): 
    return self.first_name 