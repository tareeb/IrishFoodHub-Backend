from rest_framework import serializers
from .models import User, Writer, Recipe, Testimonial, Review, Comment, Favorite , Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

class RecipeSerializer(serializers.ModelSerializer):
    writer_name = serializers.CharField(source='writer.name', read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'price', 'name', 'writer', 'writer_name' , 'image_url' , 'rec']

class WriterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Writer
        fields = ['id', 'name']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'user', 'text']

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    recipename = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'text', 'user', 'recipe', 'username', 'recipename']

    def get_username(self, obj):
        return obj.user.name

    def get_recipename(self, obj):
        return obj.recipe.name

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'review', 'user' , 'username']
        
    def get_username(self, obj):
        return obj.user.name

class FavoriteSerializer(serializers.ModelSerializer):
    recipename = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = ['id', 'recipe', 'user', 'recipename']

    def get_username(self, obj):
        return obj.user.name

    def get_recipename(self, obj):
        return obj.recipe.name

class OrderSerializer(serializers.ModelSerializer):
    recipename = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'recipe', 'recipename' ,  'user' , 'date' , 'status']
        
    def get_username(self, obj):
        return obj.user.name

    def get_recipename(self, obj):
        return obj.recipe.name