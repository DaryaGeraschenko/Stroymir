from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from . import models
from .forms import *


def home(request):
    return render(request, "home.html")


def tovar(request):
    tovar = models.tovarn.objects.all()
    context = {"tovar": tovar}
    return render(request, "tovar.html", context)


def tovarn(request, tovarn_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            tovarn = get_object_or_404(models.tovarn, id=tovarn_id)
            text = form.cleaned_data["text"]
            rating = form.cleaned_data["rating"]
            models.Review.objects.create(tovarn=tovarn, text=text, rating=rating)
            return redirect("tovarn", tovarn_id=tovarn.id)
    else:
        tovarn = get_object_or_404(models.tovarn, id=tovarn_id)
        reviews_average_rating = models.Review.objects.filter(tovarn=tovarn).aggregate(
            Avg("rating")
        )["rating__avg"]
        form = ReviewForm()
        reviews = models.Review.objects.filter(tovarn=tovarn)
        context = {
            "tovarn": tovarn,
            "reviews": reviews,
            "form": form,
            "reviews_average_rating": reviews_average_rating,
        }
        return render(request, "tovarn.html", context)


def log_in(request):
    global cleaned_data
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                username=cleaned_data["username"], password=cleaned_data["password"]
            )
            if user and user.is_active:
                login(request, user)
                return redirect("tovar")
            else:
                return HttpResponse("Something went wrong")
    else:
        form = LoginForm()
        context = {"form": form, "title": ("Login")}
        return render(request, "form.html", context)


def log_out(request):
    logout(request)
    return redirect("tovar")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User.objects.create_user(**form.cleaned_data)
            login(request, user)
            return redirect("tovar")

    else:
        form = RegistrationForm()
        context = {"form": form, "title": ("Registration")}
        return render(request, "form.html", context)