from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', DashboardLogin.as_view(),name='dashboard'),
    
    # path('',IndexView.as_view(), name='index'),
    # path('contact/',ContactView.as_view(), name='contact'),
    # path('about/', AboutView.as_view(), name='about'),
    # path('propertypage/', apartment_list, name='apartment'),
    # path('propertypage/<int:pk>/', property_details, name='')
]
