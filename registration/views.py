from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.

def register(request):
	if request.method=='POST':
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,username+' registered')
			return redirect('login')
	else:
		form=RegisterForm()
	return render(request,'registration/register.html', {'form':form})

@login_required
def profile(request):
	return render(request,'registration/profile.html')

