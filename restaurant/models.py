from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Item(models.Model):
    MENU_CHOICES = [
        ("main", "Main dishes"),
        ("breakfast", "Breakfast"),
        ("side_dish", "Side dishes"),
        ("desserts", "Desserts"),
        ("drinks", "Drinks"),
    ]

    name = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.CharField(max_length=25, choices=MENU_CHOICES, default='main')
    image_name = models.ImageField(upload_to='dishes/', blank=True, null=True)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'item')  # чтобы нельзя было добавить дубликаты

    def __str__(self):
        return f"{self.user.username} -> {self.item.name}"
