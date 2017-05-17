from django import forms
from models import Tweet

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	email = forms.EmailField(required = True)
	firstName = forms.CharField(required = True)
	lastName = forms.CharField(required = True)

	class Meta:
		model = User
		fields = ('username','firstName', 'lastName', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		password = self.cleaned_data['password1']
		user.set_password(password)
		# When using a custom form, password needs to be saved manually.

		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['firstName']
		user.last_name = self.cleaned_data['lastName']

		if commit:
			user.save()
		return user