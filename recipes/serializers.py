from rest_framework_json_api import serializers
from .models import Recipes

class ResipesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ('name', 'ingredients', 'instructions')

