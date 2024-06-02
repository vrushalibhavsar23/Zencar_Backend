
from django.db import models
from django.contrib.auth.models import AbstractUser

class Employees(AbstractUser):
    mobile_no = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True,blank=True)
    location = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employees',
        related_query_name='employee'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employees',
        related_query_name='employee'
    )

    def __str__(self):
        return self.username