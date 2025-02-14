from django.urls import path
from . import views

urlpatterns = [
    # path('', views.article_list, name='article_list'),
    # path('<uuid:pk>', views.article_detail, name='article_detail'),
    # path('add_article/', views.add_article, name='add_article'),
    # path('delete_article/<uuid:pk>', views.delete_article, name='delete_article'),
    path('', views.HomeView.as_view(), name='index'),
    path('<uuid:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('add_article/', views.AddArticleView.as_view(), name='add_article'),
    path('delete_article/<uuid:pk>', views.DeleteArticleView.as_view(), name='delete_article'),
    path('update_article/<uuid:pk>', views.UpdateArticleView.as_view(), name='update_article'),
    path('share/<uuid:pk>', views.ShareArticleView.as_view(), name='share_article'),
    path('<uuid:pk>/toggle-favorite/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
]
