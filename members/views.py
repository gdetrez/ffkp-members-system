from .models import Registration
from django.forms import ModelForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.forms.widgets import RadioSelect
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


class JoinForm(ModelForm):
    class Meta:
        model = Registration
        widgets = {
            'payment_method': RadioSelect(),
        }


def join(request):
    if request.method == 'POST': # If the form has been submitted...
        form = JoinForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            registration = form.save()
            paypal = {
                'amount': registration.contribution,
                'item_name': "ffkp membership",
                'item_number': 0,
                
                # PayPal wants a unique invoice ID
                'invoice': registration.token,
                
                # It'll be a good idea to setup a SITE_DOMAIN inside settings
                # so you don't need to hardcode these values.
                'return_url': settings.SITE_DOMAIN + reverse('return_url'),
                'cancel_return': settings.SITE_DOMAIN + reverse('cancel_url'),
                }
            form = PayPalPaymentsForm(initial=paypal)
            if settings.DEBUG:
                rendered_form = form.sandbox()
            else:
                rendered_form = form.render()
            c = RequestContext(request,
                               {'reg':registration,
                                'paypal': rendered_form})
            t = loader.get_template('pay.html')
            return HttpResponse(t.render(c))
    else:
        form = JoinForm() # An unbound form
    print form.errors
    t = loader.get_template('join.html')
    c = RequestContext(request,{
        'form': form,
    })
    return HttpResponse(t.render(c))

def paypal_cancel():
    pass

def paypal_return():
    pass
