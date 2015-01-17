__author__ = 'Harvey'

import datetime
from django.utils import timezone
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    public = models.BooleanField(default=False)
    website = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    skill_type = models.CharField(max_length=20)
    skill_detail = models.CharField(max_length=1000)
    contact_info = models.CharField(max_length=50)
    last_modify = models.DateTimeField(default=timezone.now)

    def was_modify_recently(self):
        return self.last_modify >= timezone.now() - datetime.timedelta(days=3)
