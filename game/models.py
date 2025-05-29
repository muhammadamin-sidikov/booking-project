from django.db import models
from fields.models import Field

class Game(models.Model):
    maydon = models.ForeignKey(Field, on_delete=models.CASCADE)
    sana = models.DateTimeField()
    qolgan_joy = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return f"{self.maydon.name} - {self.sana}"

