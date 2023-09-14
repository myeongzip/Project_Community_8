from django.shortcuts import render

from post.models import Post


def search(request):
        if request.method == 'POST':
                searched = request.POST['searched']        
                posts = Post.objects.filter(content__contains=searched)
                return render(request, 'searched.html', {'searched': searched, 'posts': posts})
        else:
                return render(request, 'searched.html', {})