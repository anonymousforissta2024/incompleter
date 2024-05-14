#Source: https://stackoverflow.com/questions/67081201/django-throws-attributeerror-str-object-has-no-attribute-meta-when-i-regis
from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор', related_name='posts', null=True)
    title = models.CharField(verbose_name='Заголовок объявления', max_length=255)
    text = models.TextField(verbose_name='Текст объявления')
    CATEGORIES = (
        ('T','Танки'),
        ('HM','Хилы'),
        ('DD','ДД'),
        ('TrM','Торговцы'),
        ('GM','Гилдмастеры'),
        ('QG','Квестгиверы'),
        ('FM','Кузнецы'),
        ('LM','Кожевники'),
        ('PM','Зельевары'),
        ('WM','Мастера заклинаний')
    )

    category = models.CharField(verbose_name='Категория', max_length=3, choices=CATEGORIES)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title