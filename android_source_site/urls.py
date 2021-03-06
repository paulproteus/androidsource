from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^phone-demo-page', direct_to_template, {'template': 'phone-demo-page.html'}),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

