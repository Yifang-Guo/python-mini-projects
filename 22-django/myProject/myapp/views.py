from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()

    return render(request, 'index.html', {'features' : features})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email= email).exists():
            messages.info(request, 'Email already used.')
            return redirect('register')
        else:
            user = User.objects.create_user(username= userName,  email=email, password=password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')