from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost
from .models import Product

def index(request):
  mymembers = BlogPost.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def product_list_view(request):
  mymembers = Product.objects.all().values()
  template = loader.get_template('product_list.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))