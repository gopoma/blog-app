from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # CREATE user: raise Exceptions
        # User.objects.create_user("gopoma2", "gopoma2@gmail.com", "12345")

        # Si no existe el usuario, el valor es None
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "auth/login.html", {
                    "error": True,
                    "message": "Disabled account"
                })
        else:
            return render(request, "auth/login.html", {
                "error": True,
                "message": "Invalid credentials"
            })
    
    return render(request, "auth/login.html")