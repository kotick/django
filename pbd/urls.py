from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'odclock.views.index', name='index'),
    url(r'^index$', 'odclock.views.index', name='index'),
    url(r'^crear/usuario$', 'odclock.views.crear_usuario', name='crear_usuario'),
    url(r'^ubicacion$', 'odclock.views.ubicacion', name='ubicacion'),
    url(r'^tomahora$', 'odclock.views.tomahora', name='tomahora'),
    url(r'^odclock$', 'odclock.views.quienessomos', name='quienessomos'),
    url(r'^personal$', 'odclock.views.seccionpersonal', name='seccionpersonal'),
    url(r'^login$', 'odclock.views.login_view'),
    url(r'^logout$', 'odclock.views.logout_view'),
    url(r'^borrar/hora/(\d+)/$', 'odclock.views.borrar_hora'),

    url(r'^admin/', include(admin.site.urls))
)
