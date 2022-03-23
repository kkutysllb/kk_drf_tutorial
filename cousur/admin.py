from django.contrib import admin
from .models import Cousor

# Register your models here.
@admin.register(Cousor)
class CousorAdmin(admin.ModelAdmin):
    list_display = ('name', 'introduction', 'price', 'teacher')
    search_fields = list_display
    list_filter = list_display



