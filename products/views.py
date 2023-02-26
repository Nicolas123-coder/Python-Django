from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def see_product (request):
    if request.method == 'GET':
        return render(request, 'see_product.html', {'name': 'nico'})
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
    
        product = Product(name=name, age=age)

        product.save()

        return HttpResponse('Post called')

def create_product (request) :
    return HttpResponse('create product endpoint')