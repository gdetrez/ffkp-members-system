from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url = "/join/")),
    url(r'^join/', include('join.urls', namespace='join')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve', {
                'show_indexes' : True,
                }))
