# Это созданный файл с маршрутами приложения
# он передает маршруты на основной такой же файл сайта!
from django.urls import path

from parnik_app.views import *

urlpatterns = [
    # path('', MainPage.as_view, name='home'),  # http://127.0.0.1:8000/
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('catalog/', Catalog.as_view(), name='catalog'),  # http://127.0.0.1:8000/catalog/
    path('sales/', Sales.as_view, name='sales'),  # http://127.0.0.1:8000/sales/
    path('manufacturer/', Manufact.as_view, name='manufacturer'),  # http://127.0.0.1:8000/manufacturer/
    # path('contacts/', Contacts.as_view, name='contacts'),  # http://127.0.0.1:8000/contacts/
    path('contacts/', contacts, name='contacts'),  # http://127.0.0.1:8000/contacts/
    # path('category/<slug:category_slug>', AppCategory.as_view, name='categories')
]