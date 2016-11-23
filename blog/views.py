from django.utils import timezone
from .models import Post, Categoria, Editor, Email
from .forms import LeadForm, MailForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categorias = Categoria.objects.all().order_by('nome')
    context = {'posts': posts, 'categorias':categorias}
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save_contact()
            form = LeadForm()
    else:
        form = LeadForm()
    context['form'] = form
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categorias = Categoria.objects.all().order_by('nome')
    postssemelhantes = Post.objects.all().filter(categoria=post.categoria,nivel__gt=post.nivel-1).exclude(slug=slug).order_by('nivel')
    context = {'post': post, 'categorias':categorias, 'postssemelhantes':postssemelhantes}
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save_contact()
            form = LeadForm()
    else:
        form = LeadForm()
    context['form'] = form
    return render(request, 'blog/post_detail.html', context)

def category_posts(request,slug):
    categoriaescolhida = get_object_or_404(Categoria, slug=slug)
    posts = Post.objects.all().filter(categoria=categoriaescolhida).order_by('-published_date')
    categorias = Categoria.objects.all().order_by('nome')
    context = {'posts': posts, 'categorias':categorias, 'categoriaescolhida':categoriaescolhida}
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save_contact()
            form = LeadForm()
    else:
        form = LeadForm()
    context['form'] = form
    return render(request, 'blog/post_list.html', context)

def page_mails(request):
    # users = Email.objects.get()
    context = {}
    if request.method == 'POST':
        formulario = MailForm(request.POST)
        if formulario.is_valid():
            context['is_valid'] = True
            formulario.my_send_mail()
            formulario = MailForm()
    else:
        formulario = MailForm()
    context['formulario'] = formulario
    return render(request, 'blog/page_mail.html', context)