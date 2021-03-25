from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from .models import Article
from .forms import ArticleForm
from django.utils import timezone
# Create your views here.
class ArticleListView(generic.ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class ArticleDetailView(generic.DetailView):
    model = Article

class ArticleUpdateView(LoginRequiredMixin,generic.UpdateView):
    form_class = ArticleForm
    model = Article

class ArticleCreateView(LoginRequiredMixin,generic.CreateView):
    form_class = ArticleForm
    model = Article

class DraftArticleView(LoginRequiredMixin,generic.ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(published_date__isnull=True).order_by('created_at')

def publish_article(request,slug):
    article = get_object_or_404(Article,slug=slug)
    article.publish()
    return redirect('blog:detail',slug=slug)
