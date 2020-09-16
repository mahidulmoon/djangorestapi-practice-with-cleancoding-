from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    
    #list,create,retrieve,update,partial_update,destroy
    
    class Meta:
        model = Snippet
        fields = ('title','body','created')