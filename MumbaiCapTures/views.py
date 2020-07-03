from django.shortcuts import render, redirect
from myApp.models import *
from django.db.models import Q



def get_blog_queryset(query=None):
    query_set = []
    queries = query.split(" ")
    for q in queries:
        posts = Images.objects.filter(
            Q(Title__icontains=q) |
            Q(Description__icontains=q)
        ).distinct()

        for post in posts:
            query_set.append(post)

    return list(set(query_set))


def show_home_page(request): 
    query = ""
    if request.GET:
        query = request.GET['query']
        images = get_blog_queryset(query)
        categories = Category.objects.all()
        # images = Images.objects.filter(Cat=caty)
        data = {'images':images,
                'categories':categories,
        }
        return render(request, 'home.html',data)
    images = Images.objects.all()
    categories = Category.objects.all()
    data = {'images':images,
    'categories':categories,
    }
    return render(request, 'home.html',data)


def show_category_page(request,cid):
    categories = Category.objects.all()

    caty=Category.objects.get(pk=cid)

    
    images = Images.objects.filter(Cat=caty)
    data = {'images':images,
    'categories':categories,
    }
    return render(request, 'home.html',data)
