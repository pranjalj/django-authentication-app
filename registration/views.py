from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EmailChangeForm, UsernameChangeForm, FirstNameChangeForm
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
def deleteUser(request):
	if request.method=='POST':
		try:
			user = request.user
			user.is_active = False
			user.save()
			messages.success(request, "The user is deleted")            

		except user.DoesNotExist:
			messages.error(request, "User doesnot exist")    
			return render(request, 'login')

		except Exception as e: 
			messages.error(request, "Error" + str(e))   
			return render(request, 'registration/delete_user.html')

		return redirect('logout')
	return render(request,'registration/delete_user.html')