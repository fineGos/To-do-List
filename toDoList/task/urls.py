from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'^task/$', views.AddTask.as_view(), name='task'),
    url(r'^add-list/$', views.AddList.as_view(), name='add-list'),
    url(r'^get-user/$', views.Login.as_view(), name='get-user'),
    url(r'^register/$', views.Registration.as_view(), name='register'),

    ]