from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Category, Post


POST_COUNT = 5


def get_posts_and_category_is_published():
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__date__lte=timezone.now()
    )


def index(request):
    posts = get_posts_and_category_is_published()[:POST_COUNT]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        get_posts_and_category_is_published(),
        pk=post_id
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

    post_list = (get_posts_and_category_is_published()
                 .filter(category__slug=category_slug))

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(
        request, 'blog/category.html', context
    )
