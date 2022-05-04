from django.urls import path
from execute import views

urlpatterns = [
    path('', views.RaspisanieTable.as_view(), name='home'),
    path('create', views.CreatePara.as_view(), name='create'),
]
