from django.contrib import admin

# Register your models here.
from blogs import models

admin.site.register(models.Product)
admin.site.register(models.Category)