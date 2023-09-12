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

def post_create(request):
    pass





    