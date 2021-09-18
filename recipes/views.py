import recipes
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from rest_framework import generics, serializers,status
from recipes.models import Recipes
from .serializers import ResipesSerializer


class listRecipes(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = ResipesSerializer

class DetailRecipes(generics.RetrieveAPIView):
    serializer_class = ResipesSerializer
    def get(self, request, *args, **kwargs):
        queryset = Recipes.objects.all()
        recipe = get_object_or_404(queryset , name=self.kwargs['name'])
        serializer = ResipesSerializer(recipe)
        return Response(serializer.data,status=status.HTTP_200_OK)