from rest_framework import serializers
from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serialiser for tag objects"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient Object"""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe"""

    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
        )
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'tags', 'ingredients',  'time_minutes',
                  'price', 'link',)
        read_only_fields = ('id',)
