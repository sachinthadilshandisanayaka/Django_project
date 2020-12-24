from django.shortcuts import render
from .models import Destination


# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = "Margarita"
    dest1.desc = "Nothing beats the classics! With a tomato base and mozzarella cheese sprinkled with the finest " \
                 "herbs, ypu cant say no. "
    dest1.price = 30
    return render(request, 'index.html', {'dest1': dest1})
