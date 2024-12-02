from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from oil_losses.forms import UserRegisterForm
from oil_losses.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oil_losses.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', register, name='register'),
]
