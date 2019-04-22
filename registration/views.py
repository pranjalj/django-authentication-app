from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

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

