from django.urls import path
from .views import ArticleListVieW,ArticleDetailVieW,ArticleCreateVieW,ArticleUpdateVieW,ArticleDeleteVieW

urlpatterns = [
    path('articlelist/',ArticleListVieW.as_view()),
    path('articledetails/<int:pk>/',ArticleDetailVieW.as_view()),
    path('articlecreate/',ArticleCreateVieW.as_view()),
    path('articleupdate/<int:pk>/',ArticleUpdateVieW.as_view()),
    path('articledelete/<int:pk>/',ArticleDeleteVieW.as_view()),
]