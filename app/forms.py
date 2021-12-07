from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

from django.forms import ClearableFileInput


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class NewPostForm(forms.ModelForm):
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
	tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

	class Meta:
		model = Post
		fields = ('content', 'caption', 'tags')		
