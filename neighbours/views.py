from django.shortcuts import render

def homepage(request):
    '''
    Homepage view function
    '''
    return render(request, 'neighbours/homepage.html')
