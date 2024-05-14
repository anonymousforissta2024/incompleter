#Source: https://stackoverflow.com/questions/67764955/init-takes-1-positional-argument-but-2-were-given-type-error
from django.contrib import admin
from .models import AvonleaClass

class AvonleaAdmin(admin.ModelAdmin):
    readonly_fields = ('unitDateEntered',)

admin.site.register(AvonleaClass, AvonleaAdmin)

class Birchleigh_ViewAdmin(admin.ModelAdmin):
    readonly_fields = ('unitDateEntered',)