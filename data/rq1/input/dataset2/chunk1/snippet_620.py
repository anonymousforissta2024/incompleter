#Source: https://stackoverflow.com/questions/42956867/attributeerror-function-object-has-no-attribute-views
from django.db import models
from django.db.models import permalink

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100,unique = True)
    slug = models.CharField(max_length = 100,unique = True)
    body = models.TextField()
    posted = models.DateField(db_index = True,auto_now_add = True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view-blog-post',None, {'slug' : self.slug})

class Category(models.Model):
    title = models.CharField(max_length = 100,db_index = True)
    slug = models.SlugField(max_length = 100,db_index = True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })