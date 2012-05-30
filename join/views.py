from .models import Registration
from django.forms import ModelForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.forms.widgets import RadioSelect
from django.conf import settings


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
            c = RequestContext(request, { 'reg':registration })
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
