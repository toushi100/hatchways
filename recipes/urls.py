from django.urls import path,include
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'recipes', views.listRecipes)


urlpatterns = [
    path('recipes/', views.listRecipes),
    path('recipes/detail/<name>', views.DetailRecipes.as_view()),

]