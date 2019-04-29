from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('password_change/', 
			auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),
			name='password_change'),
    path('password_change/done/', 
    		auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'), 
    		name='password_change_done'),
	path('',include('django.contrib.auth.urls')),
    path('register/', views.register,name='register'),
	path('profile/', views.profile , name='profile'),
]