from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'odclock.views.index', name='index'),
    url(r'^index$', 'odclock.views.index', name='index'),
    url(r'^login$', 'odclock.views.login_view', name='login_view'),
    url(r'^crear/usuario$', 'odclock.views.crear_usuario', name='crear_usuario'),
    url(r'^ubicacion$', 'odclock.views.ubicacion', name='ubicacion'),
    url(r'^tomahora$', 'odclock.views.tomahora', name='tomahora'),
    url(r'^odclock$', 'odclock.views.quienessomos', name='quienessomos'),
    url(r'^personal$', 'odclock.views.seccionpersonal', name='seccionpersonal'),
    url(r'^admin/', include(admin.site.urls))
)
