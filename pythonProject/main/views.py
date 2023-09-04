from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import *
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
from users.models import *
from django.core.paginator import Paginator
def menu(request, slug=None , page=1):
    if slug:
        category = Category.objects.get(slug=slug)
        product = Product.objects.filter(cat=category)
    else:

        product = Product.objects.all()
    paginator = Paginator(object_list=product, per_page=3)
    products_paginator = paginator.page(page)
    context={'category':Category.objects.all(), 'product': products_paginator}

    return render(request, 'main/menu.html', context=context)

def main(request):
    return render(request, 'main/main.html')




def detail(request,  slug):
    product_info = get_object_or_404(Product, slug=slug, available=True)

    return render(request, 'main/detail.html',  {'product':product_info})
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])