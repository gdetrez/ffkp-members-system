from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'members.views.join', name='join'),
    url(r'^paypal/return/$', 'members.views.paypal_return', name='return_url'),
    url(r'^paypal/cancel/$', 'members.views.paypal_cancel', name='cancel_url'),
    url(r'^kdkjfd/', include('paypal.standard.ipn.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve', {
                'show_indexes' : True,
                }))
