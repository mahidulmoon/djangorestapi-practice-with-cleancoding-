from django.urls import path
from .views import ArticleListVieW,ArticleDetailVieW

urlpatterns = [
    path('articlelist/',ArticleListVieW.as_view()),
    path('articledetails/<int:pk>/',ArticleDetailVieW.as_view()),
]