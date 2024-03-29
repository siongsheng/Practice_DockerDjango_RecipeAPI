from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

router = DefaultRouter()
# Names registered here will reflect in the URL
router.register('tags', views.TagViewSets)
router.register('ingredients', views.IngredientViewSets)
router.register('recipes', views.RecipeViewSets)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
