from django.urls import path,include
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'recipes', views.listRecipes)


urlpatterns = [
    path('recipes/', views.listRecipes.as_view()),
    path('recipes/<name>', views.DetailRecipes.as_view()),

]