
# Import the path function to define URL patterns
from django.urls import path
# Import the views file from the current app
from . import views

# ...existing code...
# Define URL patterns for your app
urlpatterns = [
     # Home page (Index page) – displays your learning journey
    path('', views.Index, name='index'),     # name changed to 'index'
    path('about/', views.aboutMe, name='aboutMe'),    # About Me page – shows your personal information
]

# ...existing code...