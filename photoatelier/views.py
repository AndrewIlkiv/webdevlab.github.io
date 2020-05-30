from django.shortcuts import render
from .forms import *
from .models import User


def home_view(request):
    return render(request, "index.html", {})


def about_view(request):
    return render(request, "about.html", {})


def contact_view(request):
    return render(request, "contact.html", {})


def register_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    print('user:', User.objects.all())
    return render(request, "register.html", context)


def order_view(request):
    return render(request, "order.html", {})


def stuff_view(request):
    return render(request, "stuff.html", {})
