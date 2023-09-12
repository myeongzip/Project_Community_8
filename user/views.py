from django.http import HttpResponse
from django.shortcuts import redirect, render

from user.models import User

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        User.objects.create_user(username=username, password = password, email=email, first_name=first_name, last_name=last_name)
        return redirect("")
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("Invalid request method", status=405)
    
def signin(request):
    pass