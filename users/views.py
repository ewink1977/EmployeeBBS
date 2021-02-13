from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from bbs.departments import departments

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
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

@login_required
def profileView(request, username):
    viewUser = User.objects.get(username = username)
    context = {
        'viewUser': viewUser,
        'deptList': departments,
    }
    return render(request, 'users/profile.html', context)


class profileEdit(View):
    def get(self, request, username):
        viewUser = User.objects.get(username = username)
        if request.user.userProfile.access_level >= 2 or request.user.username == username:
            context = {
                'viewUser': viewUser,
            }
            return render(request, 'users/edit_profile.html', context)
        else:
            messages.error(request, 'Sorry. You do not have access to edit this profile. Contact your supervisor if you believe this is an error.', extra_tags = 'danger')
            return redirect('userProfile', username)
    def post(self, request):
        pass