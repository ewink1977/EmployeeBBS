from django.urls import path
from users import views as UserViews

urlpatterns = [
    path('profile/edit/', UserViews.profileEdit, name = 'editUserProfile'),
    path('profile/<str:username>/', UserViews.profileView, name = 'userProfile'),
]