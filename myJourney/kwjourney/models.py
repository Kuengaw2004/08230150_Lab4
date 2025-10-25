
# Import Django's built-in model class to create database tables
from django.db import models

# Define a model to store personal information about you
class AboutMe(models.Model):
    name = models.CharField(max_length=100)  # Person's full name
    course = models.CharField(max_length=100) # Course or program the person is studying
    semester = models.CharField(max_length=50) # Current semester information
    interests = models.TextField() # Personal interests or hobbies
    email = models.EmailField()   # Email address for contact

 # This function returns the person's name as the object name in admin panel
    def __str__(self):
        return self.name

# Define a model to store details about your learning journey
class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_started = models.DateField()
    skills_gained = models.TextField()

    
    # This function returns the title as the object name in admin panel

    def __str__(self):
        return self.title
