from rest_framework import serializers
from django.contrib.auth.models import User
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','content','articleLength')



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = { 'password':{'write_only':True,'required':True} }
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user