from django.shortcuts import render, redirect
from .forms import RegisterForm, EmailChangeForm, UsernameChangeForm, FirstNameChangeForm
from social_django.models import UserSocialAuth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
user = get_user_model()


# Create your views here.

def register(request):
	if request.method=='POST':
		form=RegisterForm(request.POST)
		if form.is_valid():
			user_info = form.save(commit=False)
			first_name=form.cleaned_data.get('first_name')
			username=form.cleaned_data.get('username')
			user_info.email = username
			user_info.save()
			messages.success(request,first_name+' registered')
			return redirect('login')
	else:
		form=RegisterForm()
	return render(request,'registration/register.html', {'form':form})

@login_required
def profile(request):
	return render(request,'registration/profile.html')

@login_required
def editEmail(request):
	if request.method=='POST':
		form = EmailChangeForm(user,request.POST)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = EmailChangeForm(user)
	return render(request,'registration/change_email.html', {'form':form})

@login_required
def editUsername(request):
	if request.method=='POST':
		form = UsernameChangeForm(user,request.POST)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = UsernameChangeForm(user)
	return render(request,'registration/change_username.html', {'form':form})

@login_required
def editFirstName(request):
	if request.method=='POST':
		form = FirstNameChangeForm(user,request.POST)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = FirstNameChangeForm(user)
	return render(request,'registration/change_first_name.html', {'form':form})

@login_required
def settings(request):
	user = request.user

	try:
		github_login = user.social_auth.get(provider='github')
	except UserSocialAuth.DoesNotExist:
		github_login = None

	try:
		twitter_login = user.social_auth.get(provider='twitter')
	except UserSocialAuth.DoesNotExist:
		twitter_login = None

	try:
		facebook_login = user.social_auth.get(provider='facebook')
	except UserSocialAuth.DoesNotExist:
		facebook_login = None

	try:
		google_login = user.social_auth.get(provider='google')
	except UserSocialAuth.DoesNotExist:
		google_login = None

	can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

	return render(request, 'registration/settings.html', {
		'github_login': github_login,
		'twitter_login': twitter_login,
		'facebook_login': facebook_login,
		'google_login': google_login,
		'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/password.html', {'form': form})