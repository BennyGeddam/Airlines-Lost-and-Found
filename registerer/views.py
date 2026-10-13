from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import RegistrationFormForUser
from django.contrib.auth.forms import AuthenticationForm

# sign up function
      # auto login after registering
          # shows sign-up form
def register(request):
    if request.method == 'POST':
        form = RegistrationFormForUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('spot_items:home')
    else:
        form = RegistrationFormForUser()
    return render(request, 'registerer/signup.html', {'form': form})

# function user logina
      # login success back to home
          # Showing login form
def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('spot_items:home')
    else:
        form = AuthenticationForm()
    return render(request, 'registerer/login.html', {'form': form})

# function user logout
      # Redirects from login after to logout
def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('registerer:loginview')
    else:
        return render(request, 'registerer/logout.html')
