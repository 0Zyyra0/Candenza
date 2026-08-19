from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category


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


def post_detail(request, pid):

    post = get_object_or_404(
        Post,
        id=pid,
        status=1
    )

    context = {
        'post': post
    }

    return render(request, 'post-detail.html', context)