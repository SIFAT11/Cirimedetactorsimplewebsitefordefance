from django.contrib import admin
from .models import GDForm, Profile

@admin.register(GDForm)
class GDFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'gd_date')


admin.site.register(Profile)