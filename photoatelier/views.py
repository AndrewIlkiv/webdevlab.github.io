from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.forms import UserCreationForm
from .models import Order
from django.views.generic import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
User = get_user_model()


def home_view(request):
    return render(request, "index.html", {})


def about_view(request):
    return render(request, "about.html", {})


def contact_view(request):
    return render(request, "contact.html", {})


def order_view(request):
    return render(request, "order.html", {})


def stuff_view(request):
    return render(request, "stuff.html", {})


# def login_view(request):
#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('/')
#
#     context = {
#         'form': form,
#     }
#     return render(request, "login.html", context)
#
#
# def register_view(request):
#     next = request.GET.get('next')
#     form = UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=True)
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('/')
#
#     context = {
#         'form': form,
#     }
#     return render(request, "register.html", context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('/')


def login_page(request):
    context = {}
    return render(request, 'login.html', context)


def register_page(request):
    form = UserCreationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'register.html', context)


class OrderList(View):
    def get(self, request):
        form = OrderForm()
        orders = Order.objects.all()
        return render(request, 'order.html', context={'form': form, 'orders': orders})

    def post(self, request):
        form = OrderForm(request.POST)

        if form.is_valid():
            new_order = form.save()
            return JsonResponse({'order': model_to_dict(new_order), }, status=200)
        else:
            return redirect('order_list')


class TaskDelete(View):
    def post(self, request, id):
        order = Order.objects.get(id=id)
        order.delete()
        return JsonResponse({'result': 'ok'}, status=200)
