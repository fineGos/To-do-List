from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'^addtask/$', views.AddTask.as_view(), name='addtask'),
    ]