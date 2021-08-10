from django.db.models.query import QuerySet
from rest_framework import serializers
from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe objects"""
    ingredients = serializers.PrimaryKeyRelatedField(  # only returns IDs
        queryset=Ingredient.objects.all(), many=True)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ingredients', 'tags',
                  'time_in_minutes', 'price', 'link')
        read_only_fields = ('id',)


# Reuse code from RecipeSerializer and edit to show all details of Tag & Ingredient
class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for Recipe Detail objects"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
