from django.urls import path
from . import views 

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    
    # Каталог и категории
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:category_slug>/', views.catalog, 
         name='product_list_by_category'),
    
    # Детальная страница товара
    path('product/<slug:slug>/', views.product_detail,
         name='product_detail'),
    
    # Статические страницы 
    path('about/', views.about, name='about'),
    path('favorites/', views.favorites, name='favorites'),
    path('cart/', views.cart, name='cart'),
    
]