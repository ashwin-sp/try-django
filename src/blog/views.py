from django.http import Http404

from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm

# get -> 1 object
# filter -> []

# def blog_post_detail_page(request, slug):
#     # print(id.__class__)

#     print("DJANGO SAYS", request.method, request.path, request.user)
    
#     obj = get_object_or_404(BlogPost, slug= slug)
#     # queryset = BlogPost.objects.filter(slug= slug)
#     # if queryset.count() == 0:
#     #     raise Http404
#     # else:
#     #     obj = queryset.first()
    
#     # # try: 
#     # #     obj = BlogPost.objects.get(id=id) #query -> Database -> django render
#     # # except BlogPost.DoesNotExist: 
#     # #     raise Http404
#     # # except ValueError:
#     # #     raise Http404

    
#     template_name = 'blog_post_detail.html'
#     context = {"object": obj} 
#     return render(request, template_name, context)


def blog_post_list_view(request):
    #list out objects, can be search
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {"object_list": qs} 

    return render(request, template_name, context)

def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save(commit=False)
        obj.title = form.cleaned_data.get('title')
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {"form": form} 
    return render(request, template_name, context)

def blog_post_retrieve_view(request, slug):
    obj = get_object_or_404(BlogPost, slug= slug)
    template_name = 'blog/detail.html'
    context = {"object": obj} 
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug= slug)

    template_name = 'blog/update.html'
    context = {"object": obj, "form": None} 
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug= slug)

    template_name = 'blog/delete.html'
    context = {"object": obj, "form": None} 
    return render(request, template_name, context)