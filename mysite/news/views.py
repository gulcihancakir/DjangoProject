from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User

from .models import News, Category
from .forms import NewsForm, CategoryForm
context = {
    'categories':Category.objects.all()
}
def news_list(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    category=Category.objects.all()
    context = {
    'categories':Category.objects.all()
    }
    context['news']=news
    return render(request, 'news/news_list.html',context)


def news_detail(request: HttpRequest, pk):
    context = {
    'categories':Category.objects.all()
    }
    news = get_object_or_404(News, pk=pk)


    news.views += 1
    news.save()
    context['news']=news
    return render(request, 'news/news_detail.html', context)


def news_new(request):
    context = {
    'categories':Category.objects.all()
    }
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            form.save()
            return redirect('news_list')

    else:

        form = NewsForm()
        context['form']=form
    return render(request, 'news/news_edit.html', context)


def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST,request.FILES, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user

            form.save()
            return redirect('news_detail', pk=news.pk)

    else:

        form = NewsForm(instance=news)
    return render(request, 'news/news_edit.html', {'form': form})


def news_delete(request, pk):
    instance = News.objects.get(pk=pk)
    instance.delete()

    return redirect('news_list')


def news_dislike(request, pk):
    news = News.objects.get(pk=pk)

    news.dislike += 1

    news.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )


def news_like(request, pk):
    news = News.objects.get(pk=pk)

    news.like += 1

    news.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def category_list(request):
    context = {
    'categories':Category.objects.all()
    }
    category = Category.objects.order_by('name')
    context['category']= category
    return render(request, 'category/category_list.html', context)


def category_detail(request, pk):
    context = {
    'categories':Category.objects.all()
    }
    category = get_object_or_404(Category, pk=pk)
    context['category']=category
    return render(request, 'category/category_detail.html', context)


def category_new(request):
    context = {
    'categories':Category.objects.all()
    }
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()

            return redirect('category_list')
    else:
        form = CategoryForm()
        context['form']=form
        return render(request, 'category/category_edit.html', context)


def category_edit(request, pk):
    context = {
    'categories':Category.objects.all()
    }
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()

            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
        context['form']=form
    return render(request, 'category/category_edit.html', context)


def category_delete(request, pk):
    instance = Category.objects.get(pk=pk)
    instance.delete()
    return redirect('category_list')

# Create your views here.
