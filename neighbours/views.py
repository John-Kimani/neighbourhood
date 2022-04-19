from django.shortcuts import render
from .models import Neighborhood,Business,Post
from .forms import HoodRegistrationForm, BusinessRegistrationForm

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
    business = Business.objects.filter(neighborhood = hood).first()
    return render(request, 'neighbours/single-hood.html', {"hood":hood, 'business':business})

def join_hood(request):
    '''
    Join neighborhood view function
    '''
    form = HoodRegistrationForm()
    return render(request, 'neighbours/join-hood.html', {'form':form})


def business(request):
    '''
    Business view function
    '''
    business = Business.display_business()
    return render(request, 'neighbours/business.html', {'business':business})

def register_business(request):
    '''
    Register business
    '''
    form = BusinessRegistrationForm()
    return render(request, 'neighbours/register-business.html', {'form':form})

def view_business(request, business_id):
    '''
    View a business
    '''
    business = Business.objects.get(pk = business_id)
    return render(request, 'neighbours/single-business.html', {'business':business})

def timeline(request):
    '''
    Timeline view function
    '''
    posts = Post.objects.all()
    return render(request, 'neighbours/timeline.html', {'posts':posts})