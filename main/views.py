from django.shortcuts import render,get_object_or_404
from main import models
from main import forms
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    context={
        "articles":articles,
    }
    return render(request,'main/index.html',context)

def get_article(request,pk):
    article = get_object_or_404(models.Article,pk=pk)
    context = {
        "article":article
    }
    return render(request,'main/get_article.html',context)

def get_author(request,pk):
    author = get_object_or_404(models.Author,pk=pk)
    context={
        "author":author
    }
    return render(request ,'main/get_author.html',context)

def create_article(request):
    form = forms.CreateArticle()

    context = {
        "forms":form
    }
    if request.method=="POST":
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            form=form.save()
            return HttpResponseRedirect('/')
    return render(request,'main/create_article.html',context)

    