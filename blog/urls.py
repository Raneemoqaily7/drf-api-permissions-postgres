from django.urls import path
from blog.api.viewsets import ArticleListView ,ArticleDetailView

urlpatterns =[

    path ("article-list" , ArticleListView.as_view() ,name ="article_list"),
    path ("article-detail/<int:pk>" , ArticleDetailView.as_view() ,name ="article_detail"),
]