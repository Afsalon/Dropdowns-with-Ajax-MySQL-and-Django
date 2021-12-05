from django.urls import path
from ajapp import views

urlpatterns = [
    path('',views.HomePage.as_view(), name='home_page'),
    path('country/',views.CountryAPIView.as_view()),
    path('country/<str:name>/', views.StateAPIView.as_view()),
    path('country/<str:name>/<int:pk>/',views.CityAPIView.as_view()),
    path('middle/donothing/',views.doNothing,name='do_nothing_page'),
 ]
