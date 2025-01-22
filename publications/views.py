# publications/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from publications.models import Publication, Like, Comment
from publications.forms import PublicationForm, CommentForm

@login_required
def publication_list(request):
    publications = Publication.objects.all().select_related('user').prefetch_related('comments',
                                                                                     'comments__user', 'likes')
    publication_form = PublicationForm()
    comment_form = CommentForm()

    if request.method == 'POST':
        if 'publication_submit' in request.POST:
            publication_form = PublicationForm(request.POST)
            if publication_form.is_valid():
                publication = publication_form.save(commit=False)
                publication.user = request.user
                publication.save()
                return redirect('publications:publication_list')
        elif 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                publication_id = request.POST.get('publication_id')
                publication = get_object_or_404(Publication, id=publication_id)
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.publication = publication
                comment.save()
                return redirect('publications:publication_list')

    context = {
        'publications': publications,
        'publication_form': publication_form,
        'comment_form': comment_form,
    }
    return render(request, 'publications/publication_list.html', context)

@login_required
def like_publication(request, pk):
    publication = get_object_or_404(Publication, id=pk)
    like, created = Like.objects.get_or_create(
        user=request.user,
        publication=publication
    )

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'count': publication.likes.count()
    })

@login_required
def add_comment(request, publication_id):
    if request.method == 'POST':
        publication = get_object_or_404(Publication, id=publication_id)
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                publication=publication,
                user=request.user,
                content=content
            )
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'comment_count': publication.comments.count()
                })
    return redirect('publications:publication_list')
