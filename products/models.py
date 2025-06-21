from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    VARIANT_CHOICES = [
        ('hammer', 'Hammer'),
        ('sds_drill', 'SDS Drill'),
        ('drill_driver', 'Drill Driver'),
        ('impact_driver', 'Impact Driver'),
        ('jigsaw', 'Jigsaw'),
        ('circular_saw', 'Circular Saw'),
        ('orbital_sander', 'Orbital Sander'),
        ('tape_measure', 'Tape Measure'),
        ('hand_saw', 'Hand Saw'),
        ('pipe_cutter', 'Pipe Cutter'),
        ('pliers', 'Pliers'),
        ('wood_chisel', 'Wood Chisel'),
        ('spirit_level', 'Spirit Level'),
    ]

    variant_type = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=VARIANT_CHOICES
    )

    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ]
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class WishlistItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='wishlisted_by'
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username} ➤ {self.product.name}"
