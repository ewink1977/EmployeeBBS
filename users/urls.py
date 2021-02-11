from django.urls import path
from users import views as UserViews

urlpatterns = [
    path('profile/<str:username>/', UserViews.profileView, name = 'userProfile'),
    path('profile/<str:username>/edit/', UserViews.profileEdit.as_view(), name = 'editUserProfile'),
]