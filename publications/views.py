from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from publications.models import Publication, Like, Comment
from publications.forms import PublicationForm, CommentForm


# Vista para mostrar todas las publicaciones y permitir la creación de publicaciones, comentarios y likes
@login_required
def publication_list(request):
    # Obtener todas las publicaciones, junto con los comentarios, usuarios y likes asociados
    publications = Publication.objects.all().select_related('user').prefetch_related('comments', 'comments__user',
                                                                                     'likes')

    # Formularios para crear una nueva publicación y un comentario
    publication_form = PublicationForm()
    comment_form = CommentForm()

    # Comprobar si la petición es un POST (cuando el usuario envía un formulario)
    if request.method == 'POST':
        # Si el formulario es para crear una nueva publicación
        if 'publication_submit' in request.POST:
            publication_form = PublicationForm(request.POST)
            if publication_form.is_valid():
                # Crear la publicación, pero no la guarda inmediatamente
                publication = publication_form.save(commit=False)
                # Asociar la publicación con el usuario actual
                publication.user = request.user
                # Guardar la publicación en la base de datos
                publication.save()
                # Redirigir al usuario de nuevo a la lista de publicaciones
                return redirect('publications:publication_list')

        # Si el formulario es para crear un nuevo comentario
        elif 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                # Obtener el ID de la publicación a la que se le va a agregar el comentario
                publication_id = request.POST.get('publication_id')
                publication = get_object_or_404(Publication, id=publication_id)
                # Crear el comentario y asociarlo con el usuario y la publicación
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.publication = publication
                comment.save()
                # Redirigir a la lista de publicaciones
                return redirect('publications:publication_list')

        # Si el formulario es para agregar o quitar un like de una publicación
        elif 'like_submit' in request.POST:
            # Obtener el ID de la publicación para la cual se va a agregar o quitar el like
            publication_id = request.POST.get('publication_id')
            publication = get_object_or_404(Publication, id=publication_id)
            # Crear un like si no existe uno, o eliminarlo si ya existía
            like, created = Like.objects.get_or_create(
                user=request.user,
                publication=publication
            )
            if not created:
                like.delete()
            # Redirigir de nuevo a la lista de publicaciones
            return redirect('publications:publication_list')

    # Contexto para pasar los datos a la plantilla HTML
    context = {
        'publications': publications,  # Las publicaciones que se mostrarán
        'publication_form': publication_form,  # El formulario para crear una nueva publicación
        'comment_form': comment_form,  # El formulario para crear un comentario
    }

    # Renderizar la página con la lista de publicaciones y los formularios
    return render(request, 'publications/publication_list.html', context)
