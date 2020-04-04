from django.contrib import admin

# Register your models here.

from .models import Plant, Area, SpecificArea

admin.site.register(Plant)
admin.site.register(Area)
admin.site.register(SpecificArea)
