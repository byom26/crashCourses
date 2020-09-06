from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        # print("anonymous user is true")
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        # Check whether user is using correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")