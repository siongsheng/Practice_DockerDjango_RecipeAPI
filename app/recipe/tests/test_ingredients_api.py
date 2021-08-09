from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient

from recipe.serializers import IngredientSerializer

INGREDIENTS_URL = reverse('recipe:ingredient-list')


class PublicIngredientsApiTests(TestCase):
    """Test the publicly available Ingredients APIs"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test login required when retrieving Ingredients"""
        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateIngredientsApiTests(TestCase):
    """Test the private available Ingredients APIs"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='test123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_Ingredient_list(self):
        """Test that ingredients can be retrieved"""
        Ingredient.objects.create(name='Apple', user=self.user)
        Ingredient.objects.create(name='Pear', user=self.user)
        res = self.client.get(INGREDIENTS_URL)

        ingredients = Ingredient.objects.all().order_by('-name')
        serializer = IngredientSerializer(ingredients, many=True)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_user_Ingredient_list(self):
        """Test that retrieved ingredients are limited to authenticated user"""
        user2 = get_user_model().objects.create_user(
            email='abcd@gmail.com',
            password='testingpassword'
        )
        Ingredient.objects.create(user=user2, name='Tumeric')
        ingredient = Ingredient.objects.create(user=self.user, name='Kale')
        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)
