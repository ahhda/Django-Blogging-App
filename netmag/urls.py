from django.conf.urls import patterns,include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'netmag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.index'),
    url(r'^login/$', 'blog.views.login_user'),
    url(r'^(?P<slug>[\w\-]+)/$','blog.views.post'),
)
