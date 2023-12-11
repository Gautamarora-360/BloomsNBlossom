from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
from django.db.models import Q
from .models import Blogpost

    
def search(request):
    query = request.GET.get('search')
    query = query.lower()
    search_results = Blogpost.objects.filter(Q(title__icontains=query) | Q(heading0=query) | Q(heading1=query) | Q(heading2=query))
    params = {'search_results': search_results}
    return render(request, 'blog/search.html', params)

def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts':myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request, 'blog/blogpost.html', {'post':post})