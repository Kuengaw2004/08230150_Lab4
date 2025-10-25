from django.shortcuts import render
from .models import AboutMe, LearningJourney

def Index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'Index.html', {'journeys': journeys})

def aboutMe(request):
    abouts = AboutMe.objects.all()
    return render(request, 'aboutMe.html', {'abouts': abouts})
