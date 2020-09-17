from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('title','draft','publish','read_time','user')
        #depth =1

    def get_user(self,obj):
        return str(obj.user.username)



    
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','draft','publish','read_time')
        
    