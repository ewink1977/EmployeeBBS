from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.decorators import login_required
# Department List Dictionary Import!
from bbs.departments import departments

@login_required
def eventView(request):
    return render(request, 'events/event_single.html')

def editEvent(request):
    pass

def deleteEvent(request):
    pass

class createEvent(View):
    def get(self, request):
        context = {
            'deptList': departments
        }
        return render(request, 'events/event_add.html', context)
    
    def post(self, request):
        pass