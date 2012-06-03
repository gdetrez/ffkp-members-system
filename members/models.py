from django.db import models
import datetime


class Member(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def valid_member(self):
        today = datetime.date.today()
        return self.memberships.filter(
            valid_since__lte=today,
            valid_until__gte=today).exists()
    valid_member.boolean = True
        
default_membership_begin = datetime.date.today

def default_membership_end():
    today = datetime.date.today()
    if today.month >= 10:
        return datetime.date(today.year+1, 12, 31)
    else:
        return datetime.date(today.year, 12, 31)


class Membership(models.Model):
    member = models.ForeignKey(Member, related_name='memberships')
    valid_since = models.DateField(default=default_membership_begin)
    valid_until = models.DateField(default=default_membership_end)
    comments = models.TextField(blank=True)

    def isValid(self):
        today = datetiem.date.today()
        return self.valid_since <= today and valid_until >= today

    def __unicode__(self):
        return u"%d membership for %s" % (self.valid_until.year, self.member.name)
