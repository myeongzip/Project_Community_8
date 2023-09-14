from datetime import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm

from post.models import Comment, Post
from user.models import User

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def post_read(request):
    
    user_profile = User.objects.all()

    post_list = Post.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(post_list, 3)
    page = paginator.get_page('page')
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

# def comment_read(request):
#     # post의 id와 comment의 post id가 같다면 if 문?
#     comment_list = Comment.objects.all()
#     return render(request, 'post/detail.html', {'comment_list': comment_list})


def comment_create(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('comment_content')
        comment = Comment(post=post, content=content, user=request.user)
        comment.save()
        return redirect(f'/post/{post_id}/')
    return redirect('/user/signin/')


# @require_POST
# def comment_create(request, post_id):# 파라미터를 post_id 값을 못 가져오는 이슈
#     if request.user.is_authenticated:
#         post = get_object_or_404(Post, pk=post_id)
#         comments = Comment.objects.filter(post = post_id)
#         if request.method == "POST":
#             comment = Comment()
#             comment.post = post
#             comment.content = request.POST['content']
#             comment.created_at = timezone.now()
#             comment.save()
        # content = request.POST.get('comment_content')
        # comment = Comment(post=post, content=content, user=request.user)
        # comment.save()
        
        # comment_form = CommentForm(request.POST)
        # if comment_form.is_valid():
        #     comment = comment_form.save(commit=False)
        #     comment.post = post
        #     comment.user = request.user
        #     comment.save()
    #     return redirect('f"/post/{post_id}/"')
    # return redirect('/user/signin/')

    # 첫번째 시도 -> 역참조 무시
    # if request.method == "POST":
    #     # post_id = request.GET("comment.post.id")
    #     comments = Comment.objects.create(
    #         content=request.POST["comment_content"],
    #         user=request.user,            
    #     )
    #     return redirect("/")
    # else:
    #     return HttpResponse("Invalid request method", status=405)

def comment_update(request, comment_id, post_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        if request.user == comment.user:
            comment.content = request.POST["content"]
            comment.save()
            return redirect(f"/post/{post_id}/")
        else:
            return HttpResponse("You are not allowed to delete this todo", status=403)
    elif request.method == "GET":
        comment = Comment.objects.get(id=comment_id)
        context = {
            "comment":comment,   
        }
        return render(request, "post/detail.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)

@require_POST
def comment_delete(request, post_id, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
    return redirect(f"/post/{post_id}/")
    # if request.method == "POST":
    #     comment = Comment.objects.get(id=comment_id)
    #     if request.user == comment.user:
    #         comment.delete()
    #         return redirect(f"/post/{post_id}/")
    #     else:
    #         return HttpResponse("Invalid request method", status=405)
