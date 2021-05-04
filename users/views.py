#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#debug
import pdb


#Forms
from users.forms import ProfileForm, SignupForm

# Create your views here.
def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            print(user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html',{'error':'Invalid username or password'})
    return render(request, 'users/login.html')


def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect('login')


def signup_view(request):
    """signup view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form':form}
    )

@login_required
def update_profile(request):
    """update a user's profile view"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            updated_data = form.cleaned_data
            profile.website = updated_data['website']
            profile.phone_number = updated_data['phone_number']
            profile.biography = updated_data['biography']
            profile.picture = updated_data['picture']
            #save
            profile.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            'form':form
            }
    )