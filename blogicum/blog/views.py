from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Category, Post


def index(request):
    post = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__date__lte=timezone.now()
    ).order_by('title')[0:5]
    return render(request, 'blog/index.html', {'post_list': post})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__date__lt=timezone.now()
        ), pk=post_id
    )

    return render(
        request, 'blog/detail.html', {'post': post}
    )


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.values(
            'title', 'description',
        ).filter(
            slug=category_slug,
            is_published=True
        )
    )

    post_list = Post.objects.filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=timezone.now()
    )

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(
        request, 'blog/category.html', context
    )
