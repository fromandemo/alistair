from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^$', 'backend.views.index'),
    url(r'^project/(?P<name>[a-zA-Z0-9-]+)/$', 'backend.views.project_detail'),
    url(r'^bio/$', 'backend.views.bio'),
    url(r'^info/$', 'backend.views.info'),
    url(r'^test/$', 'backend.views.test'),
    url(r'^admin/', include(admin.site.urls)),  ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)