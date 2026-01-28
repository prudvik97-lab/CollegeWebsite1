from django.urls import path
from .models import views

urlpatterns = [
    path('contact/', views.contact_us, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]