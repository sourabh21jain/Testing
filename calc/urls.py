from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from piston.resource import Resource
from api.handlers import BlogPostHandler

from piston.authentication import HttpBasicAuthentication
blogpost_resource = Resource(handler=BlogPostHandler)

#auth = HttpBasicAuthentication(realm="My Realm")
#ad = { 'authentication': auth }

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'calc.views.home', name='home'),
    url(r'^posts/(?P<id>\d+)$', blogpost_resource),
#    url(r'^posts/$', blogpost_resource),
    #(r'^api/', include('calc.api.urls')),
    # url(r'^calc/', include('calc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^api/$','api.views.link'),
    (r'^links/new','api.views.new'),
    (r'^links/add','api.views.add'),
    (r'^links/edit/(?P<id>\d+)','api.views.edit'),
    (r'^links/update/(?P<id>\d+)','api.views.update'),
    (r'^links/delete/(?P<id>\d+)','api.views.delete'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
