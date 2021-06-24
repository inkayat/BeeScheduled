from django.urls import path

from dbmf import views


app_name = 'dbmf'
urlpatterns = [
    path('', views.Dbmf.as_view(), name='dbmf'),
]
