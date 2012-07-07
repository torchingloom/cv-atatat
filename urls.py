from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from base import views as BaseViews
from django.contrib.auth.urls import urlpatterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns += patterns('',
    (r'^$', BaseViews.Index.as_view()),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('account.urls_registration')),
    (r'^profile/', include('account.urls_profile')),
    (r'^base/', include('base.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
