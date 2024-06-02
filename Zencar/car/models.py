from django.db import models

class CarInventory(models.Model):
    car_name = models.CharField(max_length=255)
    model_year = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.car_name} ({self.model_year})"

class CarSales(models.Model):
    car_name = models.CharField(max_length=255)
    model_year = models.IntegerField()
    sales_count = models.IntegerField()

    def __str__(self):
        return f"{self.car_name} ({self.model_year})"
