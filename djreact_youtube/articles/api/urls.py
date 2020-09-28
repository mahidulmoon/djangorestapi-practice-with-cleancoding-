from django.urls import path,include
from rest_framework import routers
from .views import UserCreateViewSet,ArticleListVieW,ArticleDetailVieW,ArticleCreateVieW,ArticleUpdateVieW,ArticleDeleteVieW,ArticleViewSet


router = routers.DefaultRouter()
router.register('articleviewset',ArticleViewSet)
router.register('createuser',UserCreateViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('articlelist/',ArticleListVieW.as_view()),
    path('articledetails/<int:pk>/',ArticleDetailVieW.as_view()),
    path('articlecreate/',ArticleCreateVieW.as_view()),
    path('articleupdate/<int:pk>/',ArticleUpdateVieW.as_view()),
    path('articledelete/<int:pk>/',ArticleDeleteVieW.as_view()),
]