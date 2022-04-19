from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from neighbours.models import Post

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
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your profile information has been updated')
            return redirect('profile')
    else :
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    subject = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/update_profile.html', subject)

@login_required()
def home_news(request):
    '''
    Stay on the loop with home news
    '''
    news = Post.objects.all()
    return render(request, 'users/home-news.html', {"news":news})