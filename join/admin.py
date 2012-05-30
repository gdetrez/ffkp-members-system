from .models import *
from django.contrib import admin

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status')

admin.site.register(Registration, RegistrationAdmin)
