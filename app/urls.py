from django.urls import path
from .import views

#urls
urlpatterns = [
    path('/login',views.loginPage, name="login"),
    path('',views.registerPage, name="register"),
    path('/insta', views.insta, name='insta'),
    path('/developer', views.developer, name='developer'),
]