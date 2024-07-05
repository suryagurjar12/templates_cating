from django.urls import path
from .views import *


urlpatterns=[
    path('home/', home, name='home'),
    # path('cars/', cars, name='cars'),
    path('Services/', Services, name='Services'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('registration',registration,name="registration")
]