from django.contrib import admin
from blog import models

admin.site.register(models.Author)
admin.site.register(models.Question)
# Register your models here.
