
from django.http import Http404
from django.shortcuts import render, redirect
#from .formulaires import DimAgroAssurancef


from home.models import Post,Slider
from .forms import PostForm
#from .models import Attendance, Course, DimAgroAssurance, FactAgriculture, Post, Slider, Student, Students, Studenttt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
#import pandas as pd

# Create your views here.


#@login_required
def home(request):
    posts=Post.objects.order_by('-id').all()
    paginator = Paginator(posts, 6)
    
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    posts_number=posts.count()
    message = f'{posts_number} posts:'
    if posts_number == 1:
        message = f'{posts_number} post:'
        
    context={
        'posts':page_object,
        #'post_number':post_number,
        'message':message
            }
    
    return render (request,'pages/index.html',context)


    

#@login_required
def detail(request, id):
    post = Post.objects.get(id=id)
    
    context={
        'post':post
    }
    return render(request,'pages/detail.html',context)

#@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    
    context = {
    'form': form,
    }
    
    return render(request,'pages/new_post.html',context)


#@login_required
def update_post(request,id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES,instance=post)
            if form.is_valid():
                form.save()
                return redirect('/')
        
        else:
            form = PostForm(instance=post)
    else:
        raise Http404
    
    context = {
        
    'form': form,
    'post':post
    }
    return render(request,'pages/update_post.html',context)


    
#@login_required 
def delete_post(request,id):
    post =Post.objects.get(id=id)
    if post.user == request.user:
        post.delete()
        return redirect('/')
    else:
            raise Http404
    
    return render(request,'pages/delete.html')


#@login_required 
def search(request):
    search = request.GET.get('search')
    posts = Post.objects.filter(Q(title__icontains = search) |
                                Q(content__icontains=search) |
                                Q(image__icontains=search)
                            )
    
    
    posts_number=posts.count()
    message = f'{posts_number} results:'
    if posts_number == 1:
        message = f'{posts_number} results:'
    
    context ={
        'posts': posts,
        'message':message, 
    }
    return render(request, 'pages/search.html',context)



def all(request):
    
    posts=Post.objects.order_by('-id').all()
    context={
        'posts':posts,
        #'post_number':post_number,
       
            }
    
    return render (request,'pages/blog.html',context)




def commun(request):


    return render (request,'pages/commun.html',)

def domaine(request):


    return render (request,'pages/domaine.html',)

def peche(request):



    return render(request,'pages/peche.html')


def foncier(request):



    return render(request,'pages/foncier.html')

def agriculture(request):



    return render(request,'pages/agriculture.html')
def sante(request):



    return render(request,'pages/sante.html')
def education(request):



    return render(request,'pages/education.html')


def tabview(request):
    #daga = DimAgroAssurancef()


    return render(request,'pages/tab.html')
