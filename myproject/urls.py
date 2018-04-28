from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/?$', login),
    url(r'^logout/?$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}),
    url(r'^$', 'cms.views.main'),
    url(r'^annotated/?$', 'cms.views.ann_main'),
    url(r'^annotated/(.+)$', 'cms.views.ann_get_page'),
    url(r'^edit/?$', 'cms.views.edit_main'),
    url(r'^edit/(.+)$', 'cms.views.edit_page'),
    url(r'^(.+)$', 'cms.views.get_page')
]