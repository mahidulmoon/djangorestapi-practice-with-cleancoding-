
from django.urls import path
from .views import PostListApiView,PostDetailAPIView

urlpatterns = [
    path('post/', PostListApiView.as_view()),
    path('detail/<int:pk>/', PostDetailAPIView.as_view()),
]
