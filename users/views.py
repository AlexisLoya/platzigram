#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#debug
import pdb

#Model
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import ProfileForm

#Exceptions
from django.db.utils import IntegrityError

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
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if (confirm_password != password):
            return render(request,
                 'users/signup.html',
                 {'error':'Password confirmation does not match'}
                 )

        #Set and save a new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
        except IntegrityError:
            return render(request,
                          'users/signup.html',
                          {'error': 'Username is already used'}
                          )
        #save profile
        profile = Profile(user=user)
        profile.save()

    return render(request,'users/signup.html')

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