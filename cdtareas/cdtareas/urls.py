from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.index'),
    url(r'^register/$','dashboard.views.nuevo_usuario', name='nuevo-usuario'),
    url(r'^login/$','dashboard.views.ingresar', name='ingresar'),
    url(r'^logout/$', 'dashboard.views.cerrar', name='cerrar'),
    url(r'^new/$', 'tareas.views.nueva_tarea', name='nueva-tarea'),
    url(r'^cargo-mistareas/$', 'tareas.views.cargo_tareas', name='cargo-mistareas'),
    url(r'^cargo-tareas/$', 'tareas.views.cargo_tareasjs', name='cargo-tareas'),
    url(r'^cargo-tareassoli/$', 'tareas.views.cargo_tareassoli', name='cargo-tareassoli'),
    url(r'^tarea/(?P<tarea_slug>[\w-]+)/$', 'tareas.views.detalle_tarea', name='detalle-tarea'),
    # Examples:
    # url(r'^$', 'cdmanager.views.home', name='home'),
    # url(r'^cdmanager/', include('cdmanager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
