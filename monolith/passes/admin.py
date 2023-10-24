from django.contrib import admin
from .models import Resort
# Register your models here.


@admin.register(Resort)
class ResortAdmin(admin.ModelAdmin):
    pass
