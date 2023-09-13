from django.http import HttpResponse
from django.shortcuts import redirect, render
# from post.models import PostLikes
from django.contrib.auth.decorators import login_required
from post.models import Post
from user.models import User


# Create your views here.
def post_read(request):
    post_list = Post.objects.all()
    user_profile = User.objects.all()
    return render(request, 'post/post_list.html', {'post_list': post_list,
                                                   'user_profile': user_profile
                                                   })

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
        return render(request, "post/post_create.html")
    else:
        return HttpResponse("Invalid request method", status=405)
    


# Create your views here.
def post_read_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
            "post":post,   
        }
    return render(request, "post/detail.html", context)

def post_update(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        if request.user == post.user:
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.post_image = request.POST["post_image"]
            post.save()
            return redirect(f"/post/{post_id}/")
        else:
            return HttpResponse("You are not allowed to delete this todo", status=403)
    elif request.method == "GET":
        post = Post.objects.get(id=post_id)
        context = {
            "post":post,   
        }
        return render(request, "post/update.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)


def post_delete(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        if request.user == post.user:
            post.delete()
            return redirect("/index/")
        else:
            return HttpResponse("Invalid request method", status=405)


# def post(request, id):
    
    
#     already_liked = PostLikes.objects.filter(user=request.user, post=post).count()
#     if number_of_likes > 0:
#         already_liked = True # pass this variable to your context
#     else:
#         already_liked = False # you can make this anything other than boolean


# def like_others_post(request, post_id):
#     new_like, created = PostLikes.objects.get_or_create(user=request.user, 
#                                                    post_id=post_id)
#     if not created:
#         # you may get and delete the object as the user may already liked this post before
