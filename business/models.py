__author__ = 'Harvey'

import datetime
from django.db import models
from django.utils import timezone


class Business(models.Model):
    post_user = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    industry = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)
    contact_info = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=3)
