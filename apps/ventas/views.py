from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView

def cart(request):
    return render(request, "cart.html")

def product(request):
    return render(request, "product.html")

def checkout(request):
    return render(request, "checkout.html")
