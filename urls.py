from django.conf import settings

from django.conf.urls.defaults import patterns, include, url

from trashure.models import KnickKnack

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'remake.views.home', name='home'),
    # url(r'^remake/', include('remake.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(
        regex = r'^admin/',
        view = include(admin.site.urls),
        name = "admin",
        ),

    url(
        regex = r'^trashure/$',
        view = 'trashure.views.index',
        name = 'index',
        ),

    url(
        regex = r'^trashure/(?P<knickknack_id>\d+)/$',
        view = 'trashure.views.detail',
        name = 'detail',
        ),

    url(
        regex = r'^trashure/(?P<knickknack_id>\d+)/login/$',
        view = 'trashure.views.login',
        name = 'login',
        ),

    url(
        regex = r'^trashure/(?P<knickknack_id>\d+)/login/$',
        view = 'django.contrib.auth.views.login',
        name = 'login1',
        ),

     url(
        regex = r'^trashure/treasurehunt/$',
        view = 'trashure.views.filter',
        name = 'treasurehunt',
        )
)


if settings.DEBUG:
    urlpatterns += patterns('', url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, }
        ))
