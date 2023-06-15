from django.contrib import admin

from .models import EntertainmentProperty, IndustrialProperty, ResidentialProperty

admin.site.register(EntertainmentProperty)
admin.site.register(IndustrialProperty)
admin.site.register(ResidentialProperty)
