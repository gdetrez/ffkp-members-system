from members.models import *
from django.contrib import admin

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0
    fields = ['valid_since', 'valid_until']

class SubscriptionInline(admin.TabularInline):
    model = Subscription
    extra = 0
    #fields = ['valid_since', 'valid_until', 'status']

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'email']}),
        ('Comments', {'fields': ['comments'], 'classes': ['collapse']}),
    ]
    inlines = [MembershipInline, SubscriptionInline]
    list_display = ('name', 'email', 'valid_member')

admin.site.register(Member, MemberAdmin)


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
    list_display = (unicode,)# 'email', 'valid_member')

admin.site.register(MailingList, MLAdmin)
