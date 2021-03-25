from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blog'
urlpatterns = [
    path('',views.ArticleListView.as_view(),name='list'),
    path('drafts/',views.DraftArticleView.as_view(),name='drafts'),
    path('new/',views.ArticleCreateView.as_view(),name='create'),
    path('<slug>/',views.ArticleDetailView.as_view(),name='detail'),
    path('<slug>/publish/',views.publish_article,name='publish')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
