from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
   return render(request, 'base/home.html')
def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)