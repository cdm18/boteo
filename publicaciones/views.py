from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def community_view(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(
                author=request.user,
                content=content
            )
            messages.success(request, 'Publicación creada exitosamente')
            return redirect('community')

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'publicaciones/community.html', {'posts': posts})