from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def index(request):
    messages.success(request,'Esta é uma mensagem de sucesso!')
    messages.warning(request,'Esta é uma mensagem de sucesso!')
    return render(request,'index.html')