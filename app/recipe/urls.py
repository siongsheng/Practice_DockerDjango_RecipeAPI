from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

router = DefaultRouter()
# Names registered here will reflect in the URL
router.register('taag', views.TagViewSets)
router.register('ingredientasd', views.IngredientViewSets)
router.register('recipeasd', views.RecipeViewSets)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
