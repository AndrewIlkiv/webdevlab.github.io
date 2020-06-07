from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order
from django.views.generic import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url='login')
def home_view(request):
    return render(request, "index.html", {})


@login_required(login_url='login')
def about_view(request):
    return render(request, "about.html", {})


@login_required(login_url='login')
def contact_view(request):
    return render(request, "contact.html", {})


@login_required(login_url='login')
def order_view(request):
    return render(request, "order.html", {})


@login_required(login_url='login')
def stuff_view(request):
    return render(request, "stuff.html", {})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        context = {'form': form}

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User ' + user + ' was successfully created')
                return redirect('login')
            else:
                return redirect('/')

        return render(request, 'register.html', context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile_view(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


@login_required(login_url='login')
def profile_edit_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile_edit.html', args)


class OrderList(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = OrderForm()
        orders = Order.objects.filter(user_id=request.user.id)
        return render(request, 'order.html', context={'form': form, 'orders': orders})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = request.user
            new_order.save()
            return JsonResponse({'order': model_to_dict(new_order), }, status=200)
        else:
            return redirect('order_list')


class TaskDelete(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'login'

    def post(self, request, id):
        order = Order.objects.get(id=id)
        order.delete()
        return JsonResponse({'result': 'ok'}, status=200)


@login_required(login_url='login')
def change_pass_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile_edit')
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}

        return render(request, 'password_edit.html', args)