from django.shortcuts import render

def homepage(request):
    '''
    Homepage view function
    '''
    return render(request, 'neighbours/homepage.html')


def neighboorhood(request):
    '''
    Nighbourhood view function
    '''
    return render(request, 'neighbours/hood.html')

def business(request):
    '''
    Business view function
    '''
    return render(request, 'neighbours/business.html')
