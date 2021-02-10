from django.shortcuts import render

def LogInRegisterView(request):
    return render(request, 'bbs/login_registration.html')
