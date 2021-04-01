from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Entry, Comments
from .forms import CommentForm, SearchForm
from django.views.decorators.http import require_POST
from django.contrib import messages


def category_detail(request, name):
    category = get_object_or_404(Category, name=name)
    category_list    = category.posts.all()
    paginator = Paginator(category_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category-detail.html', context)


def index(request):
    object_list     = Post.objects.all()
    paginator       = Paginator(object_list, 3)
    page            = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, slug):
    posts = Post.objects.order_by('-create_date')[:3]
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    entries = post.entries.all()
    return render(request, 'blog/post-detail.html', {'posts': posts, 'post': post,
                                                     'entries': entries, 'comments': comments, })


@require_POST
@login_required
def comments_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.post = post
            inst.user = request.user
            inst.save()
            messages.success(request, 'کامنت شما ثبت شد.')
            return redirect("blog:post-detail", args=[post.slug])
        messages.error(request, 'خظا در ثبت کامنت.')
        return redirect("blog:post-detail", args=[post.slug])


def post_search(request):
    if 'q' in request.GET:
        form = SearchForm(request.GET)
        query = request.GET.get('q')
        if form.is_valid():
            posts = Post.objects.filter(title__icontains=query)
            return render(request, 'blog/search.html', {'posts': posts})
    return render(request, 'blog/search.html')
