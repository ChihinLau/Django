from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here. ID, Name, Speaker, Venue, Duration
class talkModel(models.Model):
	ID=models.AutoField(primary_key=True)
	Name=models.CharField(max_length=100)
	Speaker=models.CharField(max_length=100)
	Venue=models.CharField(max_length=100)
	Duration = models.DurationField()


	def __str__(self):
		return self.ID
