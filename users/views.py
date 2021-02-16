from django.shortcuts import render, redirect
from users.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from bbs.departments import departments
from posts.models import BBSPosts


def homeAuthCheck(request):
    if request.user:
        return redirect('bbsHome')
    else:
        return redirect('home')

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
    userPosts = BBSPosts.objects.filter(author = viewUser)
    context = {
        'viewUser': viewUser,
        'deptList': departments,
        'userPosts': userPosts,
    }
    return render(request, 'users/profile.html', context)

@login_required
def profileEdit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
            instance = request.user
            )
        p_form = ProfileUpdateForm(request.POST,
            request.FILES,
            instance = request.user.userProfile
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = request.user.username
            messages.success(request, f'Account updated for @{ username }!')
            return redirect('userProfile', username)
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.userProfile)
    context = {
        'viewUser': request.user,
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/edit_profile.html', context)