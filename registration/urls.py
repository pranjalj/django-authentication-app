from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('auth/', include('social_django.urls', namespace='social')),
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
	path('password_change/', 
			auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),
			name='password_change'),
    path('password_change/done/', 
    		auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'), 
    		name='password_change_done'),
    path('email_change/', views.editEmail,name='email_change'),
    path('username_change/', views.editUsername,name='username_change'),
    path('first_name_change/', views.editFirstName,name='first_name_change'),
    path('delete_user/', views.deleteUser,name='delete_user'),
	path('',include('django.contrib.auth.urls')),
    path('register/', views.register,name='register'),
	path('profile/', views.profile , name='profile'),
]