from django.urls import path
from bbs import views

urlpatterns = [
    path('', views.postsMainView, name = 'bbsHome')
]