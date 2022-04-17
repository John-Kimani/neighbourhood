from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
    '''
    New user registration
    '''
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created you can now login to your profile')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {"form":form})


def userProfile(request):
    '''
    User profile view function
    '''
    return render(request, 'users/profile.html')