from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
"""
product.objects.filter(product_id=1).delete()
product.objects.filter(product_id=2).delete()
product1 = product.objects.create(product_id=1, product_name="cola", date_created=timezone.now(), seller="Tom", product_detail="It is cola")
product1.product_name="Steak"
product1.product_detail="It is steak"
product2 = product.objects.create(product_id=2, product_name="Fish", date_created=timezone.now(), seller="Sam", product_detail="It is fish")
product1.save()
product2.save()
"""
from utils import get_db_handle, get_collection_handle
db_handle, mongo_client = get_db_handle("django", "localhost", 27017, "darkdarkb", "gundamrx782")
collection_handle = get_collection_handle(db_handle, "productapp_product")
#collection_handle.insert( { product_name: "card", product_detail: "15" } )



def home(request):
	#return HttpResponse("<h1>product home</h1>")
	context = {
		"products":product.objects.all()
		#"products":products
	}
	return render(request, "productapp/home.html", context)

def about(request):
	#return HttpResponse("<h1>product about</h1>")
	return render(request, "productapp/about.html", {"title":"about"})

class CategoryListView(ListView):
	template_name = "productapp/category.html"
	context_object_name = "products"
	def get_queryset(self):
		content = {
			"cate":self.kwargs["category"],
			"products":product.objects.filter(category__name=self.kwargs["category"]).filter(status="published")
		}

class ProductListView(ListView):
	model = product
	template_name = "productapp/home.html"
	context_object_name = "products"
	ordering = ["product_id"]

class ProductDetailView(DetailView):
	model = product
	template_name = "productapp/product_detail.html"

#class ProductCreateView(LoginRequiredMixin, CreateView):
class ProductCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
    #redirect_field_name = 'home'
	model = product
	template_name = "productapp/product_create.html"
	fields = ["product_name", "product_detail", "product_image", "catetgory" ]
	def form_valid(self, form): # set seller to the user
		form.instance.seller = self.request.user
		return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = product
	template_name = "productapp/product_create.html"
	fields = ["product_name", "product_detail", "product_image", "catetgory" ]
	def form_valid(self, form): # set seller to the user
		form.instance.seller = self.request.user
		return super().form_valid(form)
	def test_func(self):
		product=self.get_object()
		if self.request.user == product.seller:
			return True
		return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = product
	template_name = "productapp/product_delete.html"
	success_url="/"
	def form_valid(self, form): # set seller to the user
		form.instance.seller = self.request.user
		return super().form_valid(form)
	def test_func(self):
		product=self.get_object()
		if self.request.user == product.seller:
			return True
		return False

