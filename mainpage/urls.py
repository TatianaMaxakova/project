from django.urls import path
from . import views 
 
urlpatterns = [ 
    path('',          views.index,    name='mainpage'),
    path('contacts/', views.contacts, name='contacts'),
    path('about_us/', views.about_us, name='about_us'),
    # Calendar view
    path('calender/', views.calender,      name='calender_now'),
    # Calendar view
    path('calender/<str:dtstr>/', views.calender,      name='calender'),
    path('services/', views.services, name='services'),
]