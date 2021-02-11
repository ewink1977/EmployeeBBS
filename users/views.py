from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            # messages.success(request, f'Welcome, @{ user.username }! You have successfully logged in!')
            # return redirect('bbsHome')
        else:
            messages.error(request, f'Log in has failed. Either create an account or contact your supervisor for help.', extra_tags = 'danger')
            return redirect('home')
    else:
        messages.error(request, f"Invalid access attempt. If you're trying to log in, please try again, otherwise contact your supervisor.", extra_tags = 'danger')
        return redirect('home')

def Logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('home')

def Register(request):
    RegistrationForm = RegisterForm()
    if request.method == 'POST':
        RegistrationForm = RegisterForm(request.POST)
        if RegistrationForm.is_valid():
            RegistrationForm.save()
            username = RegistrationForm.cleaned_data.get('username')
            messages.success(request, f'Account created for @{ username }! You can now log in.')
            return redirect('home')
    else:
        RegistrationForm = RegisterForm()
    return render(request, 'users/register.html', { 'RegForm': RegistrationForm })