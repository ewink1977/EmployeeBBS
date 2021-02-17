from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from events.models import storeEvent
# Department List Dictionary Import!
from bbs.departments import departments

@login_required
def allEventsView(request):
    if request.user.userProfile.department >= 6:
        eventFilter = storeEvent.objects.order_by('-start_date')
    else:
        eventFilter = storeEvent.objects.order_by('-start_date').filter(department = 8 or request.user.userProfile.department)
    context = {
        'deptList': departments,
        'events': eventFilter,
    }
    return render(request, 'events/event_main.html', context)

@login_required
def eventView(request, eventID):
    context = {
        'deptList': departments,
        'event': storeEvent.objects.get(id = eventID)
    }
    return render(request, 'events/event_single.html', context)

class editEvent(View):
    def get(self, request, eventID):
        if not request.user.userProfile.access_level >= 2:
            messages.error(request, 'Sorry, you do not have permission to edit events.', extra_tags = 'danger')
            return redirect('eventHome')
        else:
            event = storeEvent.objects.get(id = eventID)
            context = {
                'event': event,
                'deptList': departments
            }
            return render(request, 'events/event_update.html', context)

    def post(self, request, eventID):
        eventToUpdate = storeEvent.objects.get(id = eventID)
        eventToUpdate.title = request.POST['eventTitle']
        eventToUpdate.description = request.POST['eventDesc']
        eventToUpdate.start_date = request.POST['eventStart']
        eventToUpdate.end_date = request.POST['eventEnd']
        eventToUpdate.department = request.POST['eventDept']
        eventToUpdate.save()
        messages.success(request, f'Event #{ eventID } has been successfully updated!')
        return redirect('eventView', eventID)

def deleteEvent(request):
    if request.method == 'POST':
        eventToDelete = storeEvent.objects.get(id = request.POST['eventID'])
        eventToDelete.delete()
        messages.success(request, 'Event has been deleted!')
        return redirect('eventHome')
    else:
        messages.error(request, 'Sorry, you do not have permission to do this.', extra_tags = 'danger')
        return redirect('eventHome')

class createEvent(View):
    def get(self, request):
        if not request.user.userProfile.access_level >= 2:
            messages.error(request, 'Sorry, you do not have permission to edit events.', extra_tags = 'danger')
            return redirect('eventHome')
        context = {
            'deptList': departments
        }
        return render(request, 'events/event_add.html', context)
    
    def post(self, request):
        poster = request.user
        eventTitle = request.POST['eventTitle']
        newEvent = storeEvent.objects.create(
            title = eventTitle,
            description = request.POST['eventDesc'],
            start_date = request.POST['eventStart'],
            end_date = request.POST['eventEnd'],
            department = request.POST['eventDept'],
            poster = poster
        )
        newEvent.save()
        messages.success(request, f'Event {eventTitle} has been added!')
        return redirect('eventView', newEvent.pk)