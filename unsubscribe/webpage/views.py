from django.shortcuts import render
from .models import przyczynaWypisania
import datetime


# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def wyslij_opinie(request):
    if request == 'POST':
        dzisiaj = str(datetime.date.today())
        
        przyczynaWypisania.objects.create(
            kiedy_dodany=dzisiaj,
            za_duzo=0,
            tresc_nieinteresuje=0,
            czyszczenie_skrzynki=0,
            inne=0,
        )
