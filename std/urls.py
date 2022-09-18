from django.urls import path,include
from std import views
urlpatterns = [
    path('skills/',views.skills,name='skills'),

]