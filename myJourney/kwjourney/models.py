from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    interests = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_started = models.DateField()
    skills_gained = models.TextField()

    def __str__(self):
        return self.title
