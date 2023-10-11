from django.contrib import admin
from .models import PolicProfile

@admin.register(PolicProfile)
class PolicProfileAdmin(admin.ModelAdmin):
    list_display = ('policeid', 'full_name', 'email', 'age', 'phone', 'gender', 'status')
    list_filter = ('status', 'gender')
    search_fields = ('policeid', 'full_name', 'email')
