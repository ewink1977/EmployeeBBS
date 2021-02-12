from django.urls import path
from events import views

urlpatterns = [
    path('', views.eventView),
    path('create/', views.createEvent.as_view())
]