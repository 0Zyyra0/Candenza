from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category
from django.http import JsonResponse


def index_view(request):

    posts = Post.objects.filter(status=1)

    search = request.GET.get('search')
    category_id = request.GET.get('category')

    if search:
        posts = posts.filter(title__icontains=search)

    if category_id:
        posts = posts.filter(category__id=category_id)

    posts = posts.order_by('-created_date')

    paginator = Paginator(posts, 4)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
        'categories': categories,
        'search': search,
        'category_id': category_id,
    }

    return render(request, 'index.html', context)



    post = get_object_or_404(
        Post,
        id=pid,
        status=1
    )

    context = {
        'post': post
    }

    return render(request, 'post-detail.html', context) 



    posts = Post.objects.filter(status=1)

    search = request.GET.get('search')
    category_id = request.GET.get('category')
    page_number = request.GET.get('page', 1)

    if search:
        posts = posts.filter(title__icontains=search)

    if category_id:
        posts = posts.filter(category__id=category_id)

    posts = posts.order_by('-created_date')

    paginator = Paginator(posts, 4)

    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
    }

    html = render(
        request,
        'partials/blog_posts.html',
        context
    ).content.decode('utf-8')

    return JsonResponse({
        'html': html,
        'has_next': page_obj.has_next(),
        'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
    })

    posts = Post.objects.filter(status=1)

    search = request.GET.get('search')
    category_id = request.GET.get('category')
    page_number = request.GET.get('page', 1)

    if search:
        posts = posts.filter(title__icontains=search)

    if category_id:
        posts = posts.filter(category__id=category_id)

    posts = posts.order_by('-created_date')

    paginator = Paginator(posts, 4)

    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
    }

    return render(
        request,
        'partials/blog_posts.html',
        context
    )
def post_detail(request, pid):

    post = get_object_or_404(
        Post,
        id=pid,
        status=1
    )

    previous_post = (
        Post.objects
        .filter(status=1, created_date__lt=post.created_date)
        .order_by('-created_date')
        .first()
    )

    next_post = (
        Post.objects
        .filter(status=1, created_date__gt=post.created_date)
        .order_by('created_date')
        .first()
    )

    related_posts = (
        Post.objects
        .filter(
            status=1,
            category__in=post.category.all()
        )
        .exclude(id=post.id)
        .distinct()
        .order_by('-created_date')[:3]
    )

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'related_posts': related_posts,
    }

    return render(
        request,
        'post-detail.html',
        context
    )
def load_more_posts(request):

    posts = Post.objects.filter(status=1)

    search = request.GET.get('search')
    category_id = request.GET.get('category')
    page_number = request.GET.get('page', 1)

    if search:
        posts = posts.filter(title__icontains=search)

    if category_id:
        posts = posts.filter(category__id=category_id)

    posts = posts.order_by('-created_date')

    paginator = Paginator(posts, 4)

    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
    }

    html = render(
        request,
        'partials/blog_posts.html',
        context
    ).content.decode('utf-8')

    return JsonResponse({
        'html': html,
        'has_next': page_obj.has_next(),
        'next_page': page_obj.next_page_number()
        if page_obj.has_next()
        else None,
    })