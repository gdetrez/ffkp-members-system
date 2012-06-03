from .models import *
from django.contrib import admin

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'status')

admin.site.register(Registration, RegistrationAdmin)
