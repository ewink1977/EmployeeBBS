from django.urls import path
from events import views

urlpatterns = [
    path('', views.allEventsView, name = 'eventHome'),
    path('view/<int:eventID>', views.eventView, name = 'eventView'),
    path('create/', views.createEvent.as_view(), name = 'createEvent'),
    path('edit/<int:eventID>', views.editEvent.as_view(), name = 'editEvent'),
    path('delete/', views.deleteEvent, name = 'deleteEvent'),
]