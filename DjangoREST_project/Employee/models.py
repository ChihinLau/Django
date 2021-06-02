from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class employee(models.Model):
	employee_id=models.AutoField(primary_key=True)
	First_name=models.CharField(max_length=100)
	Last_name=models.CharField(max_length=100)
	Department=models.CharField(max_length=100)
	Salary=models.IntegerField()


	def __str__(self):
		return self.id

	#def get_absolute_url(self):
	#	return reverse("product-detail", kwargs={"pk": self.pk})