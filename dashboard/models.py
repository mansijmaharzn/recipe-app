from django.db import models
from django.contrib.auth.models import User

from recipe.models import Recipe


class Wishlist(models.Model):
    recipes = models.ManyToManyField(Recipe)
    user = models.OneToOneField(User, related_name='wishlists', on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist of {self.user.username}"