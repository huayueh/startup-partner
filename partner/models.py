__author__ = 'Harvey'

from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=30)
    public = models.BooleanField(default=False)
    website = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    skill_type = models.CharField(max_length=20)
    skill_detail = models.CharField(max_length=1000)
    contact_info = models.CharField(max_length=50)
