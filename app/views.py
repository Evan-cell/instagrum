from django.shortcuts import render, redirect
from.forms import CreateUserForm
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# news imports
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Stream, Post, Tag, Likes, PostFileContent
from .forms import NewPostForm
from .models import Story, StoryStream

from .models import Comment
from .forms import CommentForm


from django.contrib.auth.decorators import login_required

from django.urls import reverse
from .models import Profile


# Create your views here.
def developer(request):
   return render(request, 'base/home.html')
def insta(request):
   return render(request, 'base/insta.html')   
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
			
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('insta')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)