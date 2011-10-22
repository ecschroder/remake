from django.conf.urls.defaults import patterns, include, url

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
	url(r'^admin/', include(admin.site.urls)),
	
	url(
		regex = "^trashure/$",
		view = trashure.views.index,
		name = "index",
	),

	url (
		regex = "^trashure/(?P<knickknack_id>\d+)/$",
		view = trashure.views.detail,
		name = "detail",
	),
)
