from django.urls import path
from django.conf.urls import url
from . import views

app_name='staff'

urlpatterns = [
    url(r'', views.designation, name="designation"),
]