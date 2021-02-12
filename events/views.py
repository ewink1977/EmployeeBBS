from django.shortcuts import render
from events.forms import addEvent
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.decorators import login_required

@login_required
def eventView(request):
    return render(request, 'events/event_single.html')

class createEvent(View):
    def get(self, request):
        return render(request, 'events/event_add.html')
    
    def post(self, request):
        pass