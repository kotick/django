from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'odclock.views.index', name='index'),
    url(r'^index$', 'odclock.views.index', name='index'),
    url(r'^sesionpaciente$', 'odclock.views.iniciosesionpaciente', name='iniciosesionpaciente'),
    url(r'^sesionpersonal$', 'odclock.views.iniciosesionpersonal', name='iniciosesionpersonal'),
    url(r'^crear/usuario$', 'odclock.views.crear_usuario'),
    url(r'^modificar/password$', 'odclock.views.cambiarpass'),
    url(r'^modificar/correo$', 'odclock.views.cambiaremail'),
    url(r'^modificar/telefonocelular$', 'odclock.views.cambiartelefonoc'),
    url(r'^modificar/telefonofijo$', 'odclock.views.cambiartelefonof'),
    url(r'^ubicacion$', 'odclock.views.ubicacion', name='ubicacion'),
    url(r'^tomahora$', 'odclock.views.tomahora', name='tomahora'),
    url(r'^odclock$', 'odclock.views.quienessomos', name='quienessomos'),
    url(r'^personal$', 'odclock.views.personal', name='personal'),
    url(r'^login$', 'odclock.views.login_view'),
    url(r'^logout$', 'odclock.views.logout_view'),
    url(r'^borrar/hora/(\d+)/$', 'odclock.views.borrar_hora'),
    url(r'^agregardentista$', 'odclock.views.agregardentista'),
    url(r'^eliminardentista$', 'odclock.views.eliminardentista'),
    url(r'^asignarespecialidad$', 'odclock.views.asignarespecialidad'),
    url(r'^ingresaroferta$', 'odclock.views.ingresaroferta'),
    url(r'^eliminaroferta$', 'odclock.views.eliminaroferta'),


    url(r'^admin/', include(admin.site.urls))
)
