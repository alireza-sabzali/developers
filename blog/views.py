from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comments
from .forms import CommentForm, SearchForm
from django.contrib import messages


def category_detail(request, name):
    category = get_object_or_404(Category, name=name)
    category_list = category.posts.all()
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
        'page': page
    }
    return render(request, 'blog/category-detail.html', context)


def index(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page': page
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.post, inst.user = post, request.user
            inst.save()
            return redirect('blog:post-detail', pk=pk)
    return render(request, 'blog/post-detail.html', {'post': post, 'comments': comments, 'form': form, })


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comments, pk=comment_id)
    if comment.user == request.user or request.user.is_superuser:
        comment.delete()
        return redirect('blog:index')
    return redirect('blog:index')


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.owner == request.user or request.user.is_superuser:
        post.delete()
        return redirect('blog:index')
    return redirect('blog:index')
