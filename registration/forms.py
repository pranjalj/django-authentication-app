from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#registration form
class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	class Meta:
		model = User
		fields = ['username','first_name','password1','password2']
		widgets = {
			'username': forms.EmailInput(attrs={'placeholder': 'Email'}),#email=username
			'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
			'password1': forms.PasswordInput(),
			'password2': forms.PasswordInput(),
		}
		labels = {
			'username':'Email-id',
			'first_name':'Name',
			'password1':'Password',
			'password2':'Confirm Password',
		}

#editing email form
class EmailChangeForm(forms.Form):
	"""
	A form that lets a user change set their email while checking for a change in the 
	e-mail.
	"""
	error_messages = {
		'email_mismatch': ("The two email addresses fields didn't match."),
		'not_changed': ("The email address is the same as the one already defined."),
	}

	new_email1 = forms.EmailField(
		label=("New email address"),
		widget=forms.EmailInput,
	)

	new_email2 = forms.EmailField(
		label=("New email address confirmation"),
		widget=forms.EmailInput,
	)

	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(EmailChangeForm, self).__init__(*args, **kwargs)

	def clean_new_email1(self):
		old_email = self.user.email
		new_email1 = self.cleaned_data.get('new_email1')
		if new_email1 and old_email:
			if new_email1 == old_email:
				raise forms.ValidationError(
				self.error_messages['not_changed'],
				code='not_changed',
				)
		return new_email1

	def clean_new_email2(self):
		new_email1 = self.cleaned_data.get('new_email1')
		new_email2 = self.cleaned_data.get('new_email2')
		if new_email1 and new_email2:
			if new_email1 != new_email2:
				raise forms.ValidationError(
				self.error_messages['email_mismatch'],
				code='email_mismatch',
				)
				return new_email2

	def save(self, commit=True):
		email = self.cleaned_data["new_email1"]
		self.user.email = email
		self.user.username = email		#changing username delete this if username is different than email
		if commit:
			self.user.save()
		return self.user

#editing username form
class UsernameChangeForm(forms.Form):
	"""
	A form that lets a user change set their username while checking for a change in the 
	username.
	"""
	error_messages = {
		'username_mismatch': ("The two username addresses fields didn't match."),
		'not_changed': ("The username address is the same as the one already defined."),
	}

	new_username1 = forms.EmailField(
		label=("New username"),
		widget=forms.EmailInput,
	)

	new_username2 = forms.EmailField(
		label=("New username confirmation"),
		widget=forms.EmailInput,
	)

	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(UsernameChangeForm, self).__init__(*args, **kwargs)

	def clean_new_username1(self):
		old_username = self.user.username
		new_username1 = self.cleaned_data.get('new_username1')
		if new_username1 and old_username:
			if new_username1 == old_usernamel:
				raise forms.ValidationError(
				self.error_messages['not_changed'],
				code='not_changed',
				)
		return new_username1

	def clean_new_username2(self):
		new_username1 = self.cleaned_data.get('new_username1')
		new_username2 = self.cleaned_data.get('new_username2')
		if new_username1 and new_username2:
			if new_username1 != new_username2:
				raise forms.ValidationError(
				self.error_messages['username_mismatch'],
				code='username_mismatch',
				)
				return new_username2

	def save(self, commit=True):
		username = self.cleaned_data["new_username1"]
		self.user.username = username
		if commit:
			self.user.save()
		return self.user

#editing first_name form
class FirstNameChangeForm(forms.Form):
	"""
	A form that lets a user change set their first_name while checking for a change in the 
	first_name.
	"""
	error_messages = {
		'first_name_mismatch': ("The two first_name addresses fields didn't match."),
		'not_changed': ("The first_name address is the same as the one already defined."),
	}

	first_name1 = forms.CharField(
		label=("New first_name"),
		widget=forms.TextInput,
	)

	first_name2 = forms.CharField(
		label=("New first_name confirmation"),
		widget=forms.TextInput,
	)

	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(FirstNameChangeForm, self).__init__(*args, **kwargs)

	def clean_new_username1(self):
		old_first_name = self.user.first_name
		new_first_name1 = self.cleaned_data.get('new_first_name1')
		if new_first_name1 and old_first_name:
			if new_first_name1 == old_first_name:
				raise forms.ValidationError(
				self.error_messages['not_changed'],
				code='not_changed',
				)
		return new_first_name1

	def clean_new_first_name2(self):
		new_first_name1 = self.cleaned_data.get('new_first_name1')
		new_first_name2 = self.cleaned_data.get('new_first_name2')
		if new_first_name1 and new_first_name2:
			if new_first_name1 != new_first_name2:
				raise forms.ValidationError(
				self.error_messages['username_mismatch'],
				code='username_mismatch',
				)
				return new_first_name2

	def save(self, commit=True):
		first_name = self.cleaned_data["new_first_name1"]
		self.user.first_name = first_name
		if commit:
			self.user.save()
		return self.user