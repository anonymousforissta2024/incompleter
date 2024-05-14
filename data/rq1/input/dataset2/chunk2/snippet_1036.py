#Source: https://stackoverflow.com/questions/49550834/typeerror-at-admin-jobs-job-add-tuple-does-not-support-the-buffer-interface
from django.contrib import admin
from .models import Job

admin.site.register(Job)