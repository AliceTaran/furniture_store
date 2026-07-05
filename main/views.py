from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})

def about(request):
    return render(request, 'main/about.html')

def catalog(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request,
                  'main/catalog.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products[:8] if not category_slug else products  
                      # На главной каталога показываем 3 товара, 
                      # в категориях - все
                  })

def favorites(request):
    return render(request, 'main/favorites.html')
def cart(request):
    return render(request, 'main/cart.html')


def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'main/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def product_list(request, category_slug=None):
    page = request.GET.get('page', 1)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 10)
    current_page = paginator.page(int(page))
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        paginator = Paginator(products.filter(category=category), 10)
        current_page = paginator.page(int(page))
    return render(request,
                  'main/product/list.html',
                  {'category':category,
                  'categories': categories,
                  'products': current_page,
                  'slug_url': category_slug})