from django.urls import path
from .import views

urlpatterns = [
    path("",views.user_Signup),
    path("login/",views.login),
    path("logout/", views.logout),
]
