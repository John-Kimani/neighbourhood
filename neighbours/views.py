from django.shortcuts import render
from .models import Neighborhood,Business

def homepage(request):
    '''
    Homepage view function
    '''
    return render(request, 'neighbours/homepage.html')


def neighboorhood(request):
    '''
    Nighbourhood view function
    '''
    neighborhood = Neighborhood.display_neighborhoods() 
    return render(request, 'neighbours/hood.html', {'hoods':neighborhood})

def business(request):
    '''
    Business view function
    '''
    return render(request, 'neighbours/business.html')
