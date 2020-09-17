from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import Post
from .serializers import PostSerializer

class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer