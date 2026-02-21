from django.shortcuts import render, get_object_or_404
from Blog.models import Article


def article_detail(request, title):
    article = get_object_or_404(Article, title=title)
    return render(request, "Blog/article_detail.html", {"article": article})
