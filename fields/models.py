from django.db import models
from users.models import User

class Field(models.Model):
    name = models.CharField(max_length=100)
    joy_soni = models.PositiveIntegerField()
    joylashuv = models.CharField(max_length=255)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    rasm = models.ImageField(upload_to='fields/', null=True, blank=True)

    def __str__(self):
        return self.name

