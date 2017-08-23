from django.conf.urls import url

from . import views

app_name = 'ex51'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
