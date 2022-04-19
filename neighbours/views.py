from django.shortcuts import redirect, render
from .models import Neighborhood,Business,Post, Hood
from .forms import HoodRegistrationForm, BusinessRegistrationForm
from django.contrib.auth.decorators import login_required

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


@login_required()
def view_hood(request, neighborhood_id):
    '''
    View hood view function
    '''
    hood = Neighborhood.objects.get(pk = neighborhood_id)
    business = Business.objects.filter(neighborhood = hood).first()
    return render(request, 'neighbours/single-hood.html', {"hood":hood, 'business':business})

@login_required()
def join_hood(request, neighborhood_id):
    '''
    Join neighborhood view function
    '''
    hood = Neighborhood.objects.get(pk = neighborhood_id)
    if request.method == 'POST':
        form = HoodRegistrationForm(request.POST)
        if form.is_valid():
            new_member = Hood()
            new_member.estate = form.cleaned_data['estate']
            new_member.occupant = form.cleaned_data['occupant']
            new_member.location = form.cleaned_data['location']
            new_member.message = form.cleaned_data['message']
            new_member.save()
            return redirect('hoodpage')
        
    else:
        form = HoodRegistrationForm()
    return render(request, 'neighbours/join-hood.html', {'form':form, "hood":hood})


@login_required()
def business(request):
    '''
    Business view function
    '''
    business = Business.display_business()
    return render(request, 'neighbours/business.html', {'business':business})

@login_required()
def register_business(request):
    '''
    Register business
    '''
    if request.method == 'POST':
        form = BusinessRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            new_business = Business()
            new_business.name = form.cleaned_data['name']
            new_business.owner = form.cleaned_data['owner']
            new_business.neighborhood = form.cleaned_data['neigbourhood']
            new_business.description = form.cleaned_data['description']
            new_business.business_img = form.cleaned_data['business_img']
            new_business.save()
            return redirect('hoodpage')
        
    else:
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