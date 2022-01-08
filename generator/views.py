from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('special'):
        characters.extend(list(string.punctuation))

    if request.GET.get('numbers'):
        characters.extend(list(string.digits))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for char in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})


def lotto(request):
    numbs = [numb for numb in range(1, 51)]
    result = sorted(random.sample(numbs, k=6))
    return render(request, 'generator/lotto.html', {'numbers': str(result)})
