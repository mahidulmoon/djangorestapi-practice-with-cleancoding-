from snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

# class SnippetViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset,many=True)
#         return Response(serializer.data)


class SnippetViewSet(viewsets.ModelViewSet):

    #list,create,retrieve,update,partial_update,destroy

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


    @action(methods=['GET'], detail=False)
    def newset(self,request):
        newset = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newset)
        return Response(serializer.data)