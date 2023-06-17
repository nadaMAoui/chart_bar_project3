from django.db import models
from .calcul import FinancialMetrics

class FinancialMetrics(models.Model):
    capitaux_propres = models.FloatField()
    financement_permanent = models.FloatField()
    autonomie_financiere = models.FloatField()
    actif_total = models.FloatField()
    dettes = models.FloatField()
    solvabilite_generale = models.FloatField()
    dettes_financement = models.FloatField()
    dettes_court_terme = models.FloatField()
    capacite_remboursement = models.FloatField()
    stocks = models.FloatField()
    creances = models.FloatField()
    theorique_actif = models.FloatField()

    def __str__(self):
        return f'Financial Metrics #{self.pk}'
