from django.urls import path
from .import views

#urls
urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login")
]