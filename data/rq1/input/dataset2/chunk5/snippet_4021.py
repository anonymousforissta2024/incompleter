#Source: https://stackoverflow.com/questions/62132107/typeerror-item-subject-is-no-iterable
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20, default = "Unknown")
    item_desc = models.TextField(default = "Empty")
    publish_date = models.DateTimeField(auto_now = True)
    price = models.CharField(max_length = 20, default = 0)
    quanty = models.CharField(max_length = 10000, default = 0)

    def __str__(self):
        return self.name + "  "

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    author_name = models.CharField(max_length = 20, unique = True)
    comment_text = models.TextField(default = "Empty")
    publish_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.author_name + "  "

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"