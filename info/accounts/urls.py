
from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
]
