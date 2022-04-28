from django.urls import path
from .views import login,home,signin

urlpatterns = [
    path('login', login,name="login"),
    path('signin', signin,name="signin"),
    path('home',home,name="home")
]