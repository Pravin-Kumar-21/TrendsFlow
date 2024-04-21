from django.urls import path, include
from . import views

app_name = "Users"

urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("login/", views.LoginView.as_view(), name="login"),
    # path(
    #     "signup/",
    # ),
]
