from django.shortcuts import render
from django.views.generic import ListView, DetailView

from parnik_app.models import Category, Product


def index(request):
    return render(request, 'parnik_app/main_page.html')


class Catalog(ListView):
    """
    Представление общего каталога товаров
    просто страница со списком категорий товаров
    если щелкнуть на категорию, будут отображены все товары данной категории
    """
    model = Category
    template_name = 'parnik_app/catalog.html'
    context_object_name = 'categories'


class ProductDetail(DetailView):
    """
    Детальное описание одного товара с возможностью оформить заказ на него
    Должна быть кнопка "оформить заказ". При нажатии перейти на страницу оформления
    """
    model = Product
    template_name = 'parnik_app/detail.html'
    context_object_name = 'product'






class ProductCategory(ListView):
    """
    Представление одной категории товаров
    """
    pass
    model = Product
    template_name = 'parnik_app/category.html'
    context_object_name = 'one_category'


def sales(request):
    return render(request, 'parnik_app/sales.html')


def contacts(request):
    return render(request, 'parnik_app/contacts.html')


def shoplist(request):
    return render(request, 'parnik_app/buy_list.html')
