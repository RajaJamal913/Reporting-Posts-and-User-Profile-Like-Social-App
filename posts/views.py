from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

@login_required
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('display_posts')
    else:
        form = PostForm()
    return render(request, 'templates/upload_post.html', {'form': form})

def display_posts(request):
    posts = Post.objects.all()
    return render(request, 'templates/display_posts.html', {'posts': posts})
