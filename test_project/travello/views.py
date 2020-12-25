from django.shortcuts import render
from .models import Destination


# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = "Margarita"
    dest1.img = "pizza.jpg"
    dest1.desc = "Nothing beats the classics! With a tomato base and mozzarella cheese sprinkled with the finest " \
                 "herbs, ypu cant say no. "
    dest1.price = 30

    dest2 = Destination()
    dest2.name = "Aussie"
    dest2.img = "pizza2.jpg"
    dest2.desc = "Bacon and eggs on a pizza! Bacon, ham, mozzarella,\
                        on a tomato base, topped with egg."
    dest2.price = 14

    dest3 = Destination()
    dest3.name = "Supreme"
    dest3.img = "pizza3.jpg"
    dest3.desc = "The supreme leader of pizza (no bias here). Salami, ham, chorizo, mushrooms,\
                        onions, capsicums, pineapple, on a tomato base and topped with mozzarella,\
                        herbs, and garlic. You can't go wrong."
    dest3.price = 12

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
