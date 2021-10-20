from django.shortcuts import render, redirect
from users.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from bbs.departments import departments
from posts.models import BBSPosts, BBSReply
from users.models import UserTimeManagement
from datetime import datetime, timedelta
import pytz


def homeAuthCheck(request):
    if request.user:
        return redirect('bbsHome')
    else:
        return redirect('login')

def Login(request):
    if request.user:
        return redirect('bbsHome')
    if request.method == 'GET':
        return redirect('login')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, f'Log in has failed. Either create an account or contact your supervisor for help.', extra_tags = 'danger')
            return redirect('login')
    else:
        messages.error(request, f"Invalid access attempt. If you're trying to log in, please try again, otherwise contact your supervisor.", extra_tags = 'danger')
        return redirect('login')

def Logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('login')

def Register(request):
    RegistrationForm = RegisterForm()
    if request.method == 'POST':
        RegistrationForm = RegisterForm(request.POST)
        if RegistrationForm.is_valid():
            RegistrationForm.save()
            username = RegistrationForm.cleaned_data.get('username')
            messages.success(request, f'Account created for @{ username }! You can now log in.')
            return redirect('login')
    else:
        RegistrationForm = RegisterForm()
    return render(request, 'users/register.html', { 'RegForm': RegistrationForm })

# vv PROFILE MANAGEMENT vv

@login_required
def profileView(request, username):
    viewUser = User.objects.get(username = username)
    userPosts = BBSPosts.objects.filter(author = viewUser, is_reply = False)
    userReplies = BBSReply.objects.filter(author = viewUser, is_reply = True)
    timeClock = UserTimeManagement.objects.filter(user = viewUser, clocked_in = False).order_by('-created_at')

    paginatedPosts = Paginator(userPosts.order_by('-created_at'), 5)
    page_number = request.GET.get('page')
    post_page_obj = paginatedPosts.get_page(page_number)

    context = {
        'viewUser': viewUser,
        'deptList': departments,
        'userPosts': post_page_obj,
        'userReplies': userReplies,
        'timeClock': timeClock,
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
            if request.user.pk == 2 or request.user.pk == 3:
                username = request.user.username
                messages.warning(request, f'The profile for @{ username } cannot be edited on the test platform to avoid shenanagins, but if this was a full production version, your changes would now be saved to the database!')
                return redirect('userProfile', username)
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

# vv TIME MANAGEMENT vv

@login_required
def allPunches(request, username):
    viewUser = User.objects.get(username = username)
    everyPunch = UserTimeManagement.objects.filter(user = viewUser, clocked_in = False)

    paginated = Paginator(everyPunch.order_by('-created_at'), 15)
    page_number = request.GET.get('page')
    page_obj = paginated.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'viewUser': viewUser,
    }
    return render(request, 'users/punch_full.html', context)

def manualClockIN(request):
    if request.method == 'POST':
        user = request.user
        POSTtime = request.POST['time']
        time = datetime.strptime(POSTtime, "%Y-%m-%dT%H:%M")
        newTime = pytz.utc.localize(time)
        adjustedTime = newTime + timedelta(hours=8)
        newPunch = UserTimeManagement.objects.create(
            user = user,
            clocked_in = True,
            time_in = adjustedTime
        )
        newPunch.save()
        messages.success(request, f'{ user.username }, you have been successfully clocked in!')
        return redirect('bbsHome')
    else:
        messages.error(request, "You can't do things this way. If you think you got this message in error, please contact IT or your supervisor.", extra_tags = 'danger')
        return redirect('bbsHome')

def manualClockOUT(request):
    if request.method == 'POST':
        user = request.user
        POSTtime = request.POST['time']
        time = datetime.strptime(POSTtime, "%Y-%m-%dT%H:%M")
        newTime = pytz.utc.localize(time)
        adjustedTime = newTime + timedelta(hours=8)
        # GET THE USER'S PUNCHES. BUT JUST THE LAST ONE.
        lastPunch = UserTimeManagement.objects.filter(user = user).last()
        # NOW ADD THE CLOCK OUT, SET THE USER TO CLOCKED OUT, AND DO SOME TIME MATH.
        lastPunch.time_out = adjustedTime
        lastPunch.clocked_in = False
        lastPunch.save()
        total_worked = lastPunch.time_out - lastPunch.time_in
        lastPunch.total = total_worked
        lastPunch.save()
        messages.success(request, f'{ user.username }, you have been successfully clocked out, and you worked { total_worked }!')
        return redirect('bbsHome')
    else:
        messages.error(request, "You can't do things this way. If you think you got this message in error, please contact IT or your supervisor.", extra_tags = 'danger')
        return redirect('bbsHome')

def clockIN(request):
    if request.method == 'POST':
        user = request.user
        time = datetime.now(pytz.utc)

        newPunch = UserTimeManagement.objects.create(
            user = user,
            clocked_in = True,
            time_in = time
        )
        newPunch.save()
        messages.success(request, f'{ user.username }, you have been successfully clocked in!')
        return redirect('bbsHome')
    else:
        messages.error(request, "You can't do things this way. If you think you got this message in error, please contact IT or your supervisor.", extra_tags = 'danger')
        return redirect('bbsHome')

def clockOUT(request):
    if request.method == 'POST':
        user = request.user
        time = datetime.now(pytz.utc)
        # GET THE USER'S PUNCHES. BUT JUST THE LAST ONE.
        lastPunch = UserTimeManagement.objects.filter(user = user).last()
        # NOW ADD THE CLOCK OUT, SET THE USER TO CLOCKED OUT, AND DO SOME TIME MATH.
        lastPunch.time_out = time
        lastPunch.clocked_in = False
        lastPunch.save()
        total_worked = lastPunch.time_out - lastPunch.time_in
        lastPunch.total = total_worked
        lastPunch.save()
        messages.success(request, f'{ user.username }, you have been successfully clocked out, and you worked { total_worked }!')
        return redirect('bbsHome')
    else:
        messages.error(request, "You can't do things this way. If you think you got this message in error, please contact IT or your supervisor.", extra_tags = 'danger')
        return redirect('bbsHome')