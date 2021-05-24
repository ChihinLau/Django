from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
"""
products=[
	{"product_id": "1",
	 "product_name": "Cola",
	 "date_created":"05/21/2021",
	 "seller": "Tom"
	},
	{"product_id": "2",
	 "product_name": "Fish",
	 "date_created":"05/21/2021",
	 "seller": "Sam"
	}

]
"""
product.objects.filter(product_id=1).delete()
product.objects.filter(product_id=2).delete()
product1 = product.objects.create(product_id=1, product_name="cola", date_created=timezone.now(), seller="Tom")
product1.product_name="Steak"
product2 = product.objects.create(product_id=2, product_name="Fish", date_created=timezone.now(), seller="Sam")
product1.save()
product2.save()

def home(request):
	#return HttpResponse("<h1>product home</h1>")
	context = {
		"products":product.objects.all()
		#"products":products
	}
	return render(request, "productapp/home.html", context)

def about(request):
	#return HttpResponse("<h1>product about</h1>")
	return render(request, "productapp/about.html")
