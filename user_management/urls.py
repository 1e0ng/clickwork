from __future__ import absolute_import
from django.conf.urls import url, include
from user_management import views

app_name = 'user_management'

urlpatterns = [
    url(r'^$', views.change_password, name="change-password"),
    url(r'^new/$', views.new_user),
]
