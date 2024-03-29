from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account, School
from django.contrib.auth import login

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

	class Meta:
		model = Account
		fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'accounttype']
		
		def clean_email(self):
			email = self.cleaned_data['email'].lower()
			try:
				user = Account.objects.get(email=email)
			except Exception as e:
				return email
			raise forms.ValidationError(f"Email {email} is already in use.")
		
class SchoolForm(forms.ModelForm):
	class Meta:
		model = School
		fields = ['name', 'vision', 'mission', 'schoolLvl', 'schoolGov', 'state', 'has_principal']	

		def clean(self):
			name = self.cleaned_data['name']
			try:
				school = School.objects.get(name=name)
			except Exception as e:
				return name
			raise forms.ValidationError(f"{name} is already in use.")


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def save(self, request):
		loguser = authenticate(email=self.cleaned_data['email'], password = self.cleaned_data['password'])
		if loguser:
			login(request, loguser)		


	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid Login")