from . import views
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryListView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#app_name="productapp"

urlpatterns = [
    path('', ProductListView.as_view(), name="product-home"),
	path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
	path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
	path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
	path("product/create/", ProductCreateView.as_view(), name="product-create"),
    path("about/", views.about, name="product-about"),
    path("category/<category>", views.CategoryListView.as_view(), name="product-category"),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)