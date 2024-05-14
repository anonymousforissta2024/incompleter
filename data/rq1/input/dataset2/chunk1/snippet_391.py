#Source: https://stackoverflow.com/questions/54380633/nameerror-name-f-is-not-defined-in-django-orm-query
Article.objects.filter((round(datetime.now(timezone.utc) - F("created_on")) / 300) * 300)