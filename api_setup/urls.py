from django.urls import path
from .views import ArticleAPIView, ArticleDetails

urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('details/<int:id>/', ArticleDetails.as_view()),
    # path('articles/', article_list),
    # path('details/<int:pk>/', article_detail),
]
