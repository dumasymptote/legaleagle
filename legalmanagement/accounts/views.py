from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                HttpResponseRedirect(reverse('main:dashboard'))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:index")