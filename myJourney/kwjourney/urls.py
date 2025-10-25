from django.urls import path
from . import views

# ...existing code...

urlpatterns = [
    path('', views.Index, name='index'),     # name changed to 'index'
    path('about/', views.aboutMe, name='aboutMe'),
]

# ...existing code...