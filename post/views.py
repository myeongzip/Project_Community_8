from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from post.models import Comment, Like, Post
from user.models import User

from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

# Create your views here.

def post_likes(request, post_id):
    # if request.user.is_authenticated:
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    # user_has_liked = post.liked_by.filter(id=user.id).exists() if user.is_authenticated else False
    if not user.is_authenticated:
        return redirect('/user/signin')
    like_exists = Like.objects.filter(user=user, post=post).exists()
    if like_exists:
        Like.objects.filter(user=user, post=post).delete()
    else:
        Like.objects.create(user=user, post=post)

    return redirect('/', post_id=post.id)

def post_read(request):
    user_profile = User.objects.all()
    post_list = Post.objects.order_by("-created_at")
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'post/post_list.html', {'post_list': post_list,
                                                   'user_profile': user_profile,
                                                   'posts': posts,
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
            post.post_image = request.FILES.get("post_image")
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





def comment_create(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('comment_content')
        comment = Comment(post=post, content=content, user=request.user)
        comment.save()
        return redirect(f'/post/{post_id}/')
    return redirect('/user/signin/')





@require_POST
def comment_delete(request, post_id, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
    return redirect(f"/post/{post_id}/")
