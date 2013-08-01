from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'odclock.views.index', name='index'),
    url(r'^login$', 'odclock.views.login_view', name='login_view'),
    url(r'^crear/usuario$', 'odclock.views.crear_usuario', name='crear_usuario'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
