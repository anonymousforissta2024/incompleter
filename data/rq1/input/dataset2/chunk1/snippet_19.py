#Source: https://stackoverflow.com/questions/62628292/django-addconstraints-raises-a-typeerror-on-postgres
class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0055_flashnews'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='flashnews',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('fteam__isnull', True), ('league__isnull', True), ('race__isnull', False), ('type', 1)), models.Q(('fteam__isnull', False), ('league__isnull', True), ('race__isnull', True), ('type', 2)), models.Q(('fteam__isnull', True), ('league__isnull', False), ('race__isnull', True), ('type', 3)), _connector='OR'), name='%(app_label)s_%(class)s_value_matches_type'),
        ),
    ]