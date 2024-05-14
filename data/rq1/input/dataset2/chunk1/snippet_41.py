#Source: https://stackoverflow.com/questions/62997157/django-filenotfounderror-errno-2-no-such-file-or-directory-when-trying
from main.randomgenerator import generatorran


class myModel:
    ...
    model_name = models.CharField(max_length=100,default=generatorran.getName())