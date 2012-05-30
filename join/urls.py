from django.conf.urls import patterns, include, url

urlpatterns = patterns('join.views',
    url(r'^$', 'join', name = 'join'),
 )
