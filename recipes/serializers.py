from rest_framework import serializers
from recipes.models import Category
from recipes.models import Comment
from users.models import User
from recipes.models import Recipe, Rating

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    recipe = serializers.PrimaryKeyRelatedField(read_only=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id", "content", "user", "recipe",
            "parent", "replies", "is_active",
            "created_at", "updated_at"
        ]
        read_only_fields = ["id", "user", "recipe", "created_at", "updated_at", "replies"]

    def get_replies(self, obj):
        # recursive replies
        return CommentSerializer(obj.replies.all(), many=True).data
    
class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # show username/email
    recipe = serializers.StringRelatedField(read_only=True)  # show recipe title

    class Meta:
        model = Rating
        fields = ["id", "user", "recipe", "score", "review", "created_at"]
        read_only_fields = ["id", "user", "recipe", "created_at"]

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Rating
        fields = ["id", "user", "score", "review", "created_at"]
        read_only_fields = ["id", "user", "created_at"]


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            "id", "author", "category", "title", "description",
            "ingredients", "instructions", "image",
            "is_draft", "created_at", "updated_at", "average_rating",
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at", "average_rating"]

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return sum(r.score for r in ratings) / ratings.count()

        return None