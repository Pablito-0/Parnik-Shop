from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from parnik_app.models import *
from parnik_app.utils import menu



def index(request):
    return render(request, 'parnik_app/main_page.html')


class Catalog(ListView):
    model = Category
    template_name = 'parnik_app/catalog.html'
    context_object_name = 'categories'




class Sales(ListView):
    pass




# class Contacts(ListView):
#     pass
def contacts(request):
    return render(request, 'parnik_app/index.html')
