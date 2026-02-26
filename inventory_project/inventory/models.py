from django.db import models

class Inventory_items(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)