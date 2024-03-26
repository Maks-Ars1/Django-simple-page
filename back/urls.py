from django.urls import path
from . import views

app_name = 'back'

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.post_data, name='success')
]