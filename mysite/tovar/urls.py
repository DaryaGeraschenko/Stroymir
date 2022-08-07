from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("tovar/", views.tovar, name="tovar"),
    path("tovarn/<int:tovarn_id>/", views.tovarn, name="tovarn"),
    path("register/", views.register, name="register"),
]
