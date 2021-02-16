from django.urls import path
from users import views as UserViews

urlpatterns = [
    path('clock_in/', UserViews.clockIN, name = 'clockIN'),
    path('clock_out/', UserViews.clockOUT, name = 'clockOUT'),
    path('manual/clock_in/', UserViews.manualClockIN, name='manualClockIN'),
    path('manual/clock_out/', UserViews.manualClockOUT, name='manualClockOUT'),
    path('profile/edit/', UserViews.profileEdit, name = 'editUserProfile'),
    path('profile/<str:username>/', UserViews.profileView, name = 'userProfile'),
]