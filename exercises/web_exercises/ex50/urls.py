from django.conf.urls import url

from . import views

app_name = 'ex50'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
