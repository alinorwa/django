from django.shortcuts import render , get_object_or_404
from django.http import JsonResponse
from .models import *
from .form import CommentForm

# Create your views here.
def all_posts(request):
    posts = Post.objects.all()
    data = {
        'posts':posts
    }
    return render(request , 'blog/all_posts.html',data)

def detail(request,pk):
    post = get_object_or_404(Post , pk=pk)
    data = {
        'post':post
    }
    return render(request , 'blog/detail.html',data)


def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(pk=post_id)
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return JsonResponse({'success': True})  # Send JSON response indicating success
    return JsonResponse({'success': False, 'errors': form.errors})  # Send JSON response with errors if form is not valid