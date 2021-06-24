from django.urls import path
from django.conf.urls import url


from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('open-source/', views.OpenSourceView.as_view(), name='open_source'),
    path('about/', views.AboutPage.as_view(), name='about'),
  	path('signup/', views.SignUpPage.as_view(), name='signup'),
    url('taken_course/', views.TakenCourseView.as_view(), name='taken_course'),
    url('rate_lecturer/', views.RateLecturer.as_view(), name='rate_lecturer'),
    url('profile/', views.Profile.as_view(), name='profile'),
    url('create_schedule/', views.CreateSchedule.as_view(), name='create_schedule'),
    url('schedule_generator/', views.GeneratorSchedule.as_view(), name='schedule_generator'),

]
