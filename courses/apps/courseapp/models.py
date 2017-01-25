from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    course = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
