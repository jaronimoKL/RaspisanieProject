from django.urls import path

from execute import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
]
