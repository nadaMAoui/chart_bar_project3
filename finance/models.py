
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Bilan(models.Model):
    actif_immobilisé = models.FloatField()
    stock = models.FloatField(default=0)
    créances = models.FloatField(default=0)
    trésorerie_actif = models.FloatField(default=0)
    capitaux_propre = models.FloatField(default=0)
    dette_de_financement = models.FloatField(default=0)
    dette_à_court_terme = models.FloatField(default=0)
    type = models.CharField(max_length=266)
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str_(self):
        return self.type

    class Meta:
        ordering = ['-date']    


class Type(models.Model):
        name = models.CharField(max_length=255)        

        def __str__(self):
             return self.name