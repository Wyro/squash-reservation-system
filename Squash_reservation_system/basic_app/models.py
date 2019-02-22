from django.db import models
from django.contrib.auth.models import User
#from PIL import ImageField
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)

    #profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class CourtEvent(models.Model):

    name = models.CharField('Event Name', max_length = 120)
    event_day = models.CharField('Event Date', max_length = 120)
    event_time = models.TimeField("Event Time")

    #def __str__(self):
    #    return {self.name, self.event_day, self.event_time}
