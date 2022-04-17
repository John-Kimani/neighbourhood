from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required()
def userProfile(request):
    '''
    User profile view function
    '''
    return render(request, 'users/profile.html')

@login_required()
def update_user_profile(request):
    '''
    User profile view function
    '''
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()
    subject = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/update_profile.html', subject)