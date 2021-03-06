#bu asosiy url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('product',include('product.urls')),
    path('',include('home.urls')),# '' - bu home
    path('faq/', views.faq, name='faq'),
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='about'),
    path('search/', views.search,name='search'),
    path('search_auto', views.search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>/',views.product_detail, name='product_detail'),
    path('lic/',views.lic,name='lic'),
    path('post/',views.post,name='post'),
    path('post/<int:id>/',views.post_detail, name='post_detail'),
    path('lic/<int:id>/',views.lic_detail, name='lic_detail'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)