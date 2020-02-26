from django.conf import settings
from django.conf.urls import url
from django.urls import path

from . import views
from django.views.static import serve

app_name = 'dj_cars'
urlpatterns = [
    path('', views.index, name='index')
]

url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
