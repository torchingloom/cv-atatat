from django.conf.urls.defaults import patterns, url
from account.views import *


urlpatterns = patterns('',
    url(r'^view$', ProfileOwnerView.as_view(), name='profile-view-self'),
    url(r'^view/(?P<pk>\d+)$', ProfileView.as_view(), name='profile-view'),
    url(r'^edit$', ProfileEditView.as_view(), name='profile-edit'),
)
