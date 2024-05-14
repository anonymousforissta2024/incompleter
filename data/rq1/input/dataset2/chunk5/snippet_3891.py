#Source: https://stackoverflow.com/questions/55058939/typeerror-create-got-multiple-values-for-keyword-argument-user
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from softforest.utils import unique_slug_generator

# Create your models here.

user = settings.AUTH_USER_MODEL


class Project(models.Model):
    user = models.ForeignKey(user, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    ratings = models.DecimalField(default=0.0, max_digits=50, decimal_places=2, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def modules(self):
        return self.module_set.all()


class Module(models.Model):
    project = models.ForeignKey(Project, related_name='modules', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Technology(models.Model):
    project = models.ForeignKey(Project, related_name='technologies', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Requirement(models.Model):
    project = models.ForeignKey(Project, related_name='requirements', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


def project_pre_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(project_pre_receiver, sender=Project)