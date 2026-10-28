from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ["nom","date_creation", "status","description"]
    