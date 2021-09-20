import recipes
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from rest_framework import generics, serializers,status
from recipes.models import Recipes
from .serializers import ResipesSerializer
from rest_framework.decorators import api_view

#get all recipes and post  a new recipe
@api_view(['GET', 'POST','PUT'])
def listRecipes(request,*args,**kwargs):


    if request.method == 'GET':
        queryset = Recipes.objects.all()
        serializer = ResipesSerializer(queryset, many=True)
        print(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)


    if request.method == "POST":
        name = request.data["name"]
        query = Recipes.objects.filter(name = name).exists()
        if query:
            data={"error": "Recipe already exists"}
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
        else:
            data={}
            serializer = ResipesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(data,status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        try:
            recipe = Recipes.objects.get(name=request.data['name'])
            serializer = ResipesSerializer(recipe, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        except:
            data = {"error": "Recipe does not exist"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)


#get recipe details if it exists
class DetailRecipes(generics.RetrieveAPIView):
    serializer_class = ResipesSerializer

    def get(self, request, *args, **kwargs):
        queryset = Recipes.objects.all()
        try:
            recipe = Recipes.objects.get(name=self.kwargs['name'])
            serializer = ResipesSerializer(recipe)
            print(recipe)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            data={}
            return Response(data,status=status.HTTP_200_OK)
