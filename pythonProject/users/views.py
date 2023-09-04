from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from users.models import User
from main.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from users.forms import *
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:main'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, template_name='registration/login.html', context=context)

def registration(request):
    if request.method == 'POST':

        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, template_name='registration/register.html', context=context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(x.sum() for x in baskets)
    total_quantity = sum(x.quantity for x in baskets)

    context = {'form': form,
               'basket': baskets}

    return render(request, 'registration/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))