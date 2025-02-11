from django.urls import path
from . import views




urlpatterns = [
    # path('', views.index, name = 'index'),
    path('', views.HomeView.as_view(), name='index'),
    # path('add_article/', views.add_article, name='add_article'),
    path('add_article/', views.AddArticleView.as_view(), name='add_article'),
    # path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('favorites', views.FavoritesView.as_view(), name='favorites'),
    path('article/<int:pk>/toggle-favorite/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('article/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete')
]
