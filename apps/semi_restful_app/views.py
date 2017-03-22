from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
    context = {
    "products" : Product.objects.all(),
    }
    if context is None:
        return render(request, "semi_restful_app/index.html")
    else:
        return render(request, "semi_restful_app/index.html", context)

def new (request):
    return render(request, "semi_restful_app/new.html")

def show(request, id):
    product = Product.objects.get(id=id)
    context = {
    "name" : product.name,
    "description": product.description,
    "price": product.price,
    "id": product.id
    }
    return render(request, "semi_restful_app/show.html", context)

def edit(request, id):
    product = Product.objects.get(id=id)
    context = {
    "name" : product.name,
    "description": product.description,
    "price": product.price,
    "id": product.id
    }
    return render(request, "semi_restful_app/edit.html", context)

def create(request):
    if request.method == "POST":
        Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    return redirect('/')

def update(request, id):
    product = Product.objects.get(id=id)
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.price = request.POST['price']
    product.save()
    return redirect('/')

def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')

def back(request):
    return redirect('/')
