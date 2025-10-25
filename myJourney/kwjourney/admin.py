# Import the admin module from Django

from django.contrib import admin
# Import the models you created in models.py
from .models import AboutMe, LearningJourney
# Register the AboutMe model so it appears in the Django admin site.
admin.site.register(AboutMe)
# Register the LearningJourney model so it appears in the Django admin site
admin.site.register(LearningJourney)

