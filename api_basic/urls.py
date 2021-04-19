
from django.urls import path
from .views import ArticleAPIView, ArticleDetail, GenericAPIView, article_detail, article_list

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>', article_detail),
    path('detail/<int:id>/', ArticleDetail.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]
