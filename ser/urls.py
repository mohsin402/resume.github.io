from django.urls import path,include
from ser import views
urlpatterns = [
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),

]