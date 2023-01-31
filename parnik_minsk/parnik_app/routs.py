# Это созданный файл с маршрутами приложения
# он передает маршруты на основной такой же файл сайта!
from django.urls import path

from parnik_app.views import *

urlpatterns = [
    # path('', MainPage.as_view, name='home'),  # http://127.0.0.1:8000/
    path('', index, name='home'),  # http://127.0.0.1:8000/ - главная страница
    path('catalog/', Catalog.as_view(), name='catalog'),  # http://127.0.0.1:8000/catalog/ - страница каталога
    path('sales/', sales, name='sales'),  # http://127.0.0.1:8000/sales/ - страница акций
    # path('contacts/', Contacts.as_view, name='contacts'),  # http://127.0.0.1:8000/contacts/
    path('contacts/', contacts, name='contacts'),  # http://127.0.0.1:8000/contacts/ - страница контактов
    path('shop-list/', shoplist, name='shoplist'), # http://127.0.0.1:8000/shop-list/ - страиница корзины
    path('category/<slug:category_slug>/', ProductCategory.as_view(), name='category'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product')# http://127.0.0.1:8000/contacts/ - страница товара по категории
]