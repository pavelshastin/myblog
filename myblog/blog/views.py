from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Post, Comment
from django.utils import timezone
import datetime

def index(request):
    last_reciepts = Post.objects.order_by('-published_date')[0:12]

    context = {'first_row_reciepts': last_reciepts[:4],
               'second_row_reciepts': last_reciepts[4:8],
               'third_row_reciepts': last_reciepts[8:]
               }

    return render(request, "blog/food-index.html", context)

def detail(request, post_id=1):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'blog/food-index.html', {'post': post})



def reciepts_year(request, year=2019):

    reciepts = get_list_or_404(Post, modified_date__year=year)
    months = {}

    for rec in reciepts:
        month_str = rec.modified_date.strftime("%B")
        month_num = rec.modified_date.strftime("%m")
        months.update({month_str: month_num})


    print("months", months)
    return render(request, 'blog/food-index.html', {'year': year, 'months': months})

def reciepts_month(request, year=2019, month=0):
    pass
