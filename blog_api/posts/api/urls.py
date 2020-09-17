
from django.urls import path
from .views import PostListApiView,PostDetailAPIView,PostUpdateAPIView,PostDstroyAPIView

urlpatterns = [
    path('post/', PostListApiView.as_view()),
    path('detail/<int:pk>/', PostDetailAPIView.as_view()),
    path('update/<int:pk>/', PostUpdateAPIView.as_view()),
    path('delete/<int:pk>/', PostDstroyAPIView.as_view()),
]
