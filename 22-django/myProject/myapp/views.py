from django.http import HttpResponse
from django.shortcuts import render
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very fast.'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Quality'
    feature2.details = 'Our service has very high quality.'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Reputation'
    feature3.details = 'Our service has high reputation.'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Service'
    feature4.details = 'Our service is 24/7.'

    return render(request, 'index.html', {'feature1' : feature1, 'feature2' : feature2, 'feature3' : feature3, 'feature4' : feature4})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})