from snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
# class SnippetViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset,many=True)
#         return Response(serializer.data)

class SnippetFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Snippet
        fields = ('title','created')


class SnippetViewSet(viewsets.ModelViewSet):

    #list,create,retrieve,update,partial_update,destroy

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filterset_class = SnippetFilter
    # filter_fields = ('title','created')
    # search_fields = ('id','title')
    



    @action(methods=['GET'], detail=False)
    def newset(self,request):
        newset = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newset)
        return Response(serializer.data)

    # def get_queryset(self):
    #     return Snippet.objects.filter(title_icontains='te')