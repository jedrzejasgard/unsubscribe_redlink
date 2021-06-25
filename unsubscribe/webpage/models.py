from django.db import models

# Create your models here.
class przyczynaWypisania(models.Model):
    kiedy_dodany = models.CharField(max_length=100)
    za_duzo = models.IntegerField(default=0)
    tresc_nieinteresuje = models.IntegerField(default=0)
    czyszczenie_skrzynki = models.IntegerField(default=0)
    inne = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.kiedy_dodany}'
