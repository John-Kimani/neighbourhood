from django.shortcuts import render
from .models import Neighborhood,Business

def homepage(request):
    '''
    Homepage view function
    '''
    return render(request, 'neighbours/homepage.html')


def neighboorhood(request):
    '''
    Neighbourhood view function
    '''
    neighborhood = Neighborhood.display_neighborhoods() 
    return render(request, 'neighbours/hood.html', {'hoods':neighborhood})


def view_hood(request, neighborhood_id):
    '''
    View hood view function
    '''
    hood = Neighborhood.objects.get(pk = neighborhood_id)
    return render(request, 'neighbours/single-hood.html', {"hood":hood})


def business(request):
    '''
    Business view function
    '''
    return render(request, 'neighbours/business.html')
