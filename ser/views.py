from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def services(request):
    context = {'services':'active'}
    return render(request,'ser/services.html',context)
def contact(request):
    context = {'contact':'active'}
    return render(request,'ser/contact.html',context)