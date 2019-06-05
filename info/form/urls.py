from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'form'

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
]