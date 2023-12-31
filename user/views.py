from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from user.models import User



def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        User.objects.create_user(username=username, password = password, email=email, first_name=first_name, last_name=last_name)
        return redirect("/")
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("Invalid request method", status=405)
    
def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("Invalid auth", status=401)
    
    elif request.method == "GET":
        return render(request, "user/signin.html")
    
    else:
        return HttpResponse("Invalid request method", status=405)
    
def signout(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")
    else:
        return HttpResponse("Invalid request method", status=405)
    
def mypage(request):
    if request.method == "GET":
        profile = User.objects.all()
        context = {
            "profile":profile,   
        }
        return render(request, "user/mypage.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)

    
def profile_update(request, user_id):
    if request.method == "POST":
        profile = User.objects.get(id=user_id)
        if request.user.username == profile.username:
            profile.password = request.POST["password"]
            profile.email = request.POST["email"]
            profile.image = request.FILES.get("user_image")
            profile.bio = request.POST["bio"]
            profile.save()
            return redirect("/user/mypage/")
        else:
            return HttpResponse("You are not allowed to delete this todo", status=403)
    elif request.method == "GET":
        profile = User.objects.get(id=user_id)
        if request.user.id == profile.id:
            context = {
                "profile":profile,   
            }
            return render(request, "user/profile_update.html", context)
        else:
            return HttpResponse("You are not allowed to delete this todo", status=403)
    else:
        return HttpResponse("Invalid request method", status=405)
