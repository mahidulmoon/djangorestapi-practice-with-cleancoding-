
from django.urls import path
from .views import PostListApiView

urlpatterns = [
    path('', PostListApiView.as_view()),
]
