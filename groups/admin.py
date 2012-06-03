from members.models import *
from groups.models import *
from django.contrib import admin


class ListMembersInline(admin.TabularInline):
    model = Subscription
    extra = 1
    #fields = ['member']


class MLAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['name', 'email']}),
    #     ('Comments', {'fields': ['comments'], 'classes': ['collapse']}),
    # ]
    inlines = [ListMembersInline]
    list_display = ('list_name', 'number_of_members')

admin.site.register(MailingList, MLAdmin)
