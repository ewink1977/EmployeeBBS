from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def Register(request):
    RegistrationForm = RegisterForm()
    if request.method == 'POST':
        RegistrationForm = RegisterForm(request.POST)
        if RegistrationForm.is_valid():
            username = RegistrationForm.cleaned_data.get('username')
            messages.success(request, f'Account created for @{ username }!')
            return redirect('bbsHome')
    else:
        RegistrationForm = RegisterForm()
    return render(request, 'users/register.html', { 'RegForm': RegistrationForm })