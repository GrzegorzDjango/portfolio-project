from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

#w urls jest path('<int:blog_id>/' i dlatego możemy tu użyć tego argumentu
def detail(request, blog_id):
    #szukamy konkretnego bloga
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})


