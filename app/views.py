from django.shortcuts import render, redirect
from.forms import CreateUserForm
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
   return render(request, 'base/home.html')
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)