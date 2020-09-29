from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .serializers import ArticleSerializer,UserRegistrationSerializer
from articles.models import Article
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .pagination import ListPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response

class ArticleListVieW(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailVieW(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateVieW(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdateVieW(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDeleteVieW(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (IsAuthenticated,)
    pagination_class = ListPagination
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filter_fields = ('id','title')
    search_fields = ('id','content')


    @action(detail=True,methods=['GET'])
    def newest(self,request,*args,**kwargs):
        querylist = self.get_queryset().order_by('-id')
        serializer = ArticleSerializer(querylist,many=True)
        return Response(serializer.data)



class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer