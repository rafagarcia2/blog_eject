from django.utils import timezone
from .models import Post, Categoria, Editor
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categorias = Categoria.objects.all().order_by('nome')
    return render(request, 'blog/post_list.html', {'posts': posts, 'categorias':categorias})

def post_detail(request, title):
    post = get_object_or_404(Post, title=title)
    categorias = Categoria.objects.all().order_by('nome')
    postssemelhantes = Post.objects.all().filter(categoria=post.categoria,nivel__gt=post.nivel-1).exclude(title=title).order_by('nivel')
    return render(request, 'blog/post_detail.html', {'post': post, 'categorias':categorias, 'postssemelhantes':postssemelhantes})

def category_posts(request,nome):
    categoriaescolhida = get_object_or_404(Categoria, nome=nome)
    posts = Post.objects.all().filter(categoria=categoriaescolhida).order_by('-published_date')
    categorias = Categoria.objects.all().order_by('nome')
    return render(request, 'blog/post_list.html', {'posts': posts, 'categorias':categorias, 'categoriaescolhida':categoriaescolhida})