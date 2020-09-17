from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView
from ..models import Post
from .serializers import PostSerializer,PostDetailSerializer,PostCreateSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    def parform_update(self,serializer):
        serializer.save(user=self.request.user)

class PostDstroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def parform_create(self,serializer):
        serializer.save(user=self.request.user)