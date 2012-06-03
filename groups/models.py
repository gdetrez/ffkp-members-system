from members.models import Member
from django.db import models
import datetime

class MailingList(models.Model):
    name = models.CharField(max_length=256)
    domain = models.CharField(max_length=256)
    LIST_TYPE = (
        ('N', 'Newsletter'),
        ('F', 'Forum'),
    )
    type = models.CharField(max_length=1, choices=LIST_TYPE)

    def __unicode__(self):
        return u"%s@%s" % (self.name, self.domain)

    def list_name(self):
        return u"%s@%s" % (self.name, self.domain)

    def number_of_members(self):
        return len(self.members.all())


def default_subscription_end():
    today = datetime.date.today()
    if today.month >= 10:
        return datetime.date(today.year+1, 12, 31)
    else:
        return datetime.date(today.year, 12, 31)

class Subscription(models.Model):
    member = models.ForeignKey(Member, related_name='lists')
    list = models.ForeignKey(MailingList, related_name='members')
    subscription_date = models.DateField(default = datetime.date.today, editable=False)
    expiration_date = models.DateField(default = default_subscription_end)

    def __unicode__(self):
        return u"%s to %s" % (self.member.email, self.list)
