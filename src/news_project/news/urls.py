from django.urls import path
from . import views

urlpatterns = [
    # path('', views.article_list, name='article_list'),
    # path('<uuid:pk>', views.article_detail, name='article_detail'),
    # path('add_article/', views.add_article, name='add_article'),
    # path('delete_article/<uuid:pk>', views.delete_article, name='delete_article'),
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<uuid:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('add_article/', views.AddArticleView.as_view(), name='add_article'),
    path('delete_article/<uuid:pk>', views.DeleteArticleView.as_view(), name='delete_article'),
]
