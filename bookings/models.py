from django.core.validators import MinValueValidator
from django.db import models
from users.models import User
from game.models import Game

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sana = models.ForeignKey(Game, on_delete=models.CASCADE)
    soni = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_qolgan_joy()

    def update_qolgan_joy(self):
        game = self.sana
        field = game.maydon

        jami_bron = Booking.objects.filter(sana=game).aggregate(
            total=models.Sum('soni')
        )['total'] or 1

        game.qolgan_joy = field.joy_soni - jami_bron
        game.save()

        def __str__(self):
            return f"{self.user.name} - {self.sana.maydon.name} ({self.sana.sana})"

