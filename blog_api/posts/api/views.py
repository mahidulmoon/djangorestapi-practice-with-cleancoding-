from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView
from ..models import Post
from .serializers import PostSerializer,PostDetailSerializer,PostCreateSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter
class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['id','title']
    # def get_queryset(self,*args,**kwargs):
    #     queryset_list = Post.objects.all()
    #     query = self.request.GET.get['q']
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(title_icontains=query) |
    #             Q(content_icontains=query) |
    #             Q(user__first_name__icontains=query) |
    #             Q(title__last_name_icontains=query) 
    #         ).distinct()
    #     return queryset_list



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