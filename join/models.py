from django.db import models
from django.core.exceptions import ValidationError
from uuid import uuid1


def validate_contribution(value):
    if value < 50:
        raise ValidationError(u'The minimum contribution is 50 SEK')


class Registration(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    contribution = models.IntegerField(default=50, validators=[validate_contribution])
    token = models.CharField(max_length=36, default=uuid1, unique=True, editable = False)

    STATUS_CHOICES = (
        ('P', 'Waiting for payment'),
        ('M', 'Waiting for email confirmation'),
        ('F', 'Finished'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='P', editable=False)

    def get_email_confirmation_url(self):
        return "http://ffkp.se/join/confirm/?=%s" % self.token

    def validate_payment(self, method=None, amount = None):
        if self.status != 'P':
            return True
        c = Context({'registration': registration})
        mail = loader.get_template('confirm_email.txt')
        send_mail('Please confirm your email address',
                  mail.render(c),
                  'info@ffkp.se',
                  [self.email],
                  fail_silently = True)
        self.status = 'M'
        self.save()
        return True
        
    def validate_email(self):
        if self.status == "F":
            return True
        # Create or retreive member
        try:
            member = Member.objects.get(email = self.email)
        except Member.DoesNotExists:
            member = Member(name = self.name, email = self.email)
            member.save()

        # Add membership
        Memberhip(member).save()

        # Send email
        c = Context({'member': member})
        mail = loader.get_template('welcome_email.txt')
        send_mail('Welcome to the ffkp!',
                  mail.render(c),
                  'info@ffkp.se',
                  [self.email],
                  fail_silently = True)
        self.status = 'F'
        self.save()
        return True
