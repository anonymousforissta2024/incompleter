#Source: https://stackoverflow.com/questions/50194562/django-2-0-2-problems-with-modelform-creation-attributeerror-str-object-has
class Rischi(models.Model):
    RISCHIO = (
        ('Nullo', 'Nullo'),
        ('Irrilevante', 'Irrilevante'),
        ('Basso', 'Basso'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
        )
    azienda = models.ForeignKey(
        'azienda.Azienda',
        on_delete=models.CASCADE,
        )
    foto = models.ImageField(upload_to='rischi', blank=True)
    attivita = models.ForeignKey(
        Attivita,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        )
    luogo = models.ForeignKey(
        Luoghi,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        )
    macchina = models.ForeignKey(
        Macchine,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        )
    sostanza = models.ForeignKey(
        Sostanze,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        )
    fonte_rischio = models.ForeignKey(
        Fonte_rischio,
        on_delete=models.CASCADE
        )
    pericolo = models.CharField(max_length=200)
    mansione = models.ManyToManyField(
        'mansione.Mansione'
        )
    livello_rischio = models.CharField(max_length=200)
    rischio = models.CharField(max_length=200, choices=RISCHIO)
    allegato = models.ManyToManyField(
        Allegati,
        blank=True,
        )
    note = models.TextField(blank=True)
    data_di_creazione = models.DateField(auto_now_add=True)
    data_di_modifica = models.DateField(auto_now=True)

    def __str__(self):
        return  self.fonte_rischio.nome + ", id: "+ str(self.pk)