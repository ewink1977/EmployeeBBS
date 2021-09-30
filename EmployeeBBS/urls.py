from django.contrib import admin
from django.contrib.auth import views as AuthViews
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as userView
from bbs import views as bbsView

urlpatterns = [
    path('', bbsView.landing_page),
    path('admin/', admin.site.urls),
    path('home/', AuthViews.LoginView.as_view(template_name = 'users/homepage.html'), name = 'home'),
    path('login/', userView.Login, name = 'login'), 
    path('logout/', userView.Logout, name = 'logout'),
    path('register/', userView.Register, name = 'register'),
    path('bbs/', include('bbs.urls')),
    path('events/', include('events.urls')),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)