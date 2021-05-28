from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class product(models.Model):
	product_id=models.IntegerField(primary_key = True)
	product_name=models.CharField(max_length=100)
	date_created=models.DateTimeField(auto_now_add=True)
	seller=models.CharField(max_length=100)
	product_detail=models.CharField(max_length=9999, default="")
	#seller=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("product-detail", kwargs={"pk": self.pk})


