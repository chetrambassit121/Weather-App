from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import USCities

# Register your models here.


@admin.register(USCities)
class US_Cities_admin(ImportExportModelAdmin):
    list_display = ('id', 'city', 'state', 'temperature', 'wind', 'description')
    
    # pass
