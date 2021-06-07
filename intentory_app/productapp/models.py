from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class product(models.Model):
	product_id=models.AutoField(primary_key = True)
	product_name=models.CharField(max_length=100)
	date_created=models.DateTimeField(auto_now_add=True)
	#seller=models.CharField(max_length=100)
	product_detail=models.CharField(max_length=9999, default="")
	seller=models.ForeignKey(User, on_delete=models.CASCADE)
	product_image=models.ImageField(default="default.jpg", upload_to="product_image")
	catetgory = models.CharField(max_length=999, default="None")

	def __str__(self):
		return self.product_name

	def get_absolute_url(self):
		return reverse("product-detail", kwargs={"pk": self.pk})

class Category(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("product-home")


