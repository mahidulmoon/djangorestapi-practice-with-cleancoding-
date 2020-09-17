from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView
from ..models import Post
from .serializers import PostSerializer,PostDetailSerializer,PostCreateSerializer

class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostDstroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer