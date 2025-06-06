from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email
	
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['content']
		widgets = {
			'content': forms.Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Escribe un mensaje',
				'rows': 3
			}),
		}

		
