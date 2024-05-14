#Source: https://stackoverflow.com/questions/62628292/django-addconstraints-raises-a-typeerror-on-postgres
FlashNewsTypes = [
    (1, 'Race'),
    (2, 'League'),
    (3, 'Fteam')
]


class FlashNews(models.Model):

    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=True, blank=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=True)
    fteam = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE, null=True, blank=True)
    type = models.IntegerField(choices=FlashNewsTypes, default=FlashNewsTypes[0][0])

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="unique_notnull_field",
                check=(
                    models.Q(
                        type=FlashNewsTypes[0][0],
                        race__isnull=False,
                        league__isnull=True,
                        fteam__isnull=True,
                    ) | models.Q(
                        type=FlashNewsTypes[1][0],
                        race__isnull=True,
                        league__isnull=False,
                        fteam__isnull=True,
                    ) | models.Q(
                        type=FlashNewsTypes[2][0],
                        race__isnull=True,
                        league__isnull=True,
                        fteam__isnull=False,
                    )
                ),
            )
        ]