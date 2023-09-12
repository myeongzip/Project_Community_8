from django.http import HttpResponse
from django.shortcuts import redirect, render

from post.models import Post
from user.models import User

# Create your views here.
def post_read(request):
    post_list = Post.objects.all()
    user_profile = User.objects.all()
    return render(request, 'post/post_list.html', {'post_list': post_list,
                                                   'user_profile': user_profile
                                                   })

def create(request):
    user = user=request.user
    return render(request, 'post/post_create.html')

def post_create(request):
    if request.method == "POST":
        Post.objects.create(
            content=request.POST["content"], 
            title=request.POST["title"],
            user=request.user,
            post_image = request.FILES.get("post_image")
        )
        return redirect("/post/post_read/")
    elif request.method == "GET":
        return render(request, "/post/post_read")
    else:
        return HttpResponse("Invalid request method", status=405)
    





    