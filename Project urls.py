"""
URL configuration for collegeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from collegeApp.views import home_view
from collegeApp.views import CSEView,CSE_AIML_View,CSE_Data_Science_View
from collegeApp import views


urlpatterns = [
    path('', include('collegeApp.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path("cse/", CSEView.as_view(), name="cse"),
    path('aiml/',CSE_AIML_View.as_view(),name='aiml'),
    path('cse-data-science/', CSE_Data_Science_View.as_view(), name='cse_data_science'),
    path('mechanical-engineering/', views.MechanicalEngineeringView.as_view(), name='mechanical'),
    path('civil/',views.CivilEngineeringView.as_view(),name = 'civil'),
    path('electrical/',views.ElectricalEngineeringView.as_view(),name = 'electrical'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
    path('contact/', views.ContactUsView.as_view(), name='contact'),
    path("library/", views.LibraryView.as_view(), name="library"),
    path('smartboard/', views.SmartBoardView.as_view(), name='smartboard'),
    path('hostel/', views.HostelView.as_view(), name='hostel'),
    path("transport/", views.TransportView.as_view(), name="transport"),
    path('no-ragging/', views.NoRaggingView.as_view(), name='no_ragging'),
    path('sports/', views.SportsView.as_view(), name='sports'),
    path('canteen/', views.CanteenView.as_view(), name='canteen'),
    path('infrastructure/', views.InfrastructureView.as_view(), name='infrastructure'),
    path('placements/', views.PlacementsView.as_view(), name='placements'),
    path('admission/', views.admission_view, name='admission'),
    path('admission-success/', views.admission_success, name='admission_success'),
    

]


