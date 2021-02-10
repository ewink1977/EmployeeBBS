from django.shortcuts import render, HttpResponse

def HomePageView(request):
    return HttpResponse('<h1>SUCCESS</h1>')
    # return render(request, 'bbs/home.html')
