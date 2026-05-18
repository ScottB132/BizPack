from django.db import models
from trips.models import Trip


class PackingCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g. Clothing, Tech, Documents
    icon = models.CharField(max_length=10, default='📦')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Packing Categories"


class PackingItem(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(PackingCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    packed = models.BooleanField(default=False)
    ai_generated = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({'✓' if self.packed else '○'})"
