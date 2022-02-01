from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers


from .models import Follow
from recipes.serializers import RecipeSerializer

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name'
        )


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('user', 'author')


class ListFollowingSerializer(serializers.ModelSerializer):
    recipes_count = serializers.IntegerField()
    # recipes = RecipeSerializer(many=True)
    recipes = serializers.SerializerMethodField('get_recipes')

    def get_recipes(self, obj):
        recipes_limit = self.context['request'].query_params.get('recipes_limit')
        print(recipes_limit)
        queryset = obj.recipes.all()[:int(recipes_limit)]
        print(queryset.query)
        print(dir(obj))
        return RecipeSerializer(queryset, many=True, context=self.context).data

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name',
            'recipes_count', 'recipes'
        )


class RecipeLimitSerializer(serializers.Serializer):
    recipes_limit = serializers.IntegerField(default=1)

