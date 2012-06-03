from members.models import *
from groups.models import *
from django.contrib import admin
from django.forms.models import BaseInlineFormSet, ModelForm


class AlwaysChangedModelForm(ModelForm):
    """This overrides the default forms for the membership.
    The reason is that otherwise, in the likely event that
    one wants to use the default values, the form is recognised 
    as not having chagend and the membeship is not saved.
    """
    def has_changed(self):
        """ Should returns True if data differs from initial. 
        By always returning true even unchanged inlines will get validated and saved."""
        return True

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0
    fields = ['valid_since', 'valid_until']
    form = AlwaysChangedModelForm

class SubscriptionInline(admin.TabularInline):
    model = Subscription
    extra = 0
    #fields = ['valid_since', 'valid_until']

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'email']}),
        ('Comments', {'fields': ['comments'], 'classes': ['collapse']}),
    ]
    inlines = [MembershipInline, SubscriptionInline]
    list_display = ('name', 'email', 'valid_member')

admin.site.register(Member, MemberAdmin)
