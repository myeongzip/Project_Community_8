from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from post.models import Post
from user.models import User

# Create your views here.

def post_likes(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        print("all() : ",post.likes.all())
        likes = post.likes.all()
        print("Likes : ",likes)
        print(request.user.username)
        if likes == request.user.username:
            likes.filter(User=request.user.username).delete()
        #     print("!!!!!!!!!",likes)
        #     print("???????",request.user.username)
        #     likes.objects.get(user=request.user.username).delete()
        #     likes.delete()
        else:
            print("ㅁㅓ냐.,,?",likes)
        #     # likes.user = request.user.username
        #     # likes.save()
        #     # likes.create(request.user.username)
        #     print(likes)
        return redirect('/')
    return redirect('/user/signin')

def post_read(request):
    post_list = Post.objects.order_by("-created_at") #최신순으로 ~!
    user_profile = User.objects.all()
    return render(request, 'post/post_list.html', {'post_list': post_list,
                                                   'user_profile': user_profile
                                                   })

def post_create(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            user=request.user,
            post_image = request.FILES.get("post_image")
        )
        return redirect("/")
    elif request.method == "GET":
        return render(request, "post/create.html")
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
