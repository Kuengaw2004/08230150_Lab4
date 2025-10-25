# Import the render function to display HTML templates

from django.shortcuts import render
from .models import AboutMe, LearningJourney # Import the models from models.py

# This view function displays the main page (Index.html)
# It fetches all LearningJourney objects from the database

def Index(request):
    journeys = LearningJourney.objects.all()# Get all learning journey records
    return render(request, 'Index.html', {'journeys': journeys}) # Pass data to the template
# This view function displays the About Me page (aboutMe.html)
# It fetches all AboutMe objects from the database
def aboutMe(request):
    abouts = AboutMe.objects.all()
    return render(request, 'aboutMe.html', {'abouts': abouts})
