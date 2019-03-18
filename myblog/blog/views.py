from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment

def index(request):
    last_reciepts = Post.objects.order_by('-published_date')[0:12]

    context = {'first_row_reciepts': last_reciepts[:4],
               'second_row_reciepts': last_reciepts[4:8],
               'third_row_reciepts': last_reciepts[8:]
               }

    return render(request, "blog/food-index.html", context)

def detail(request, post_id=1):
    print(post_id)
    context = {}
    return render(request, 'blog/food-single.html', context)




