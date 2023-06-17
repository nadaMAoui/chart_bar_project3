
def autonomie_financiere(capitaux_propres, financement_permanent):
    from .models_calcul import FinancialMetrics
    autonomie = capitaux_propres / financement_permanent
    FinancialMetrics.objects.create(
        capitaux_propres=capitaux_propres,
        financement_permanent=financement_permanent,
        autonomie_financiere=autonomie,
    )
    return autonomie

# Other calculation functions (solvabilite_generale, capacite_remboursement, actif_total) follow the same pattern

def autonomie_financiere(capitaux_propres, financement_permanent):
    from .models_calcul import FinancialMetrics
    """
    Calculates the financial autonomy using the formula:
    autonomie financière = capitaux_propres / financement_permanent
    """
    autonomie = capitaux_propres / financement_permanent
    FinancialMetrics.objects.create(
        capitaux_propres=capitaux_propres,
        financement_permanent=financement_permanent,
        autonomie_financiere=autonomie,
    )
    return autonomie

def solvabilite_generale(actif_total, dettes):
    from .models_calcul import FinancialMetrics
    """
    Calculates the general solvency using the formula:
    solvabilité général = actif_total / dettes
    """
    solvabilite = actif_total / dettes
    financial_metrics = FinancialMetrics.objects.create(
        actif_total=actif_total,
        dettes=dettes,
        solvabilite_generale=solvabilite,
    )
    return solvabilite


def capacite_remboursement(capitaux_propres, dettes_financement):
    from .models_calcul import FinancialMetrics
    """
    Calculates the repayment capacity using the formula:
    capacitée de remboursement = capitaux_propres / dettes_financement
    """
    capacite = capitaux_propres / dettes_financement
    financial_metrics = FinancialMetrics.objects.create(
        capitaux_propres=capitaux_propres,
        dettes_financement=dettes_financement,
        capacite_remboursement=capacite,
    )
    return capacite


def actif_total(actif_immobilise, stocks, creances, theorique_actif):
    """
    Calculates the total assets using the formula:
    actif_total = actif_immobilise + stocks + creances + theorique_actif
    """
    from .models_calcul import FinancialMetrics
    actif_total_value = actif_immobilise + stocks + creances + theorique_actif
    financial_metrics = FinancialMetrics.objects.create(
        actif_immobilise=actif_immobilise,
        stocks=stocks,
        creances=creances,
        theorique_actif=theorique_actif,
        actif_total=actif_total_value,
    )
    return actif_total_value


def total_dettes(dettes_financement, dettes_court_terme):
    """
    Calculates the total debts using the formula:
    total_des_dettes = dettes_financement + dettes_court_terme
    """
    from .models_calcul import FinancialMetrics
    total_dettes_value = dettes_financement + dettes_court_terme
    financial_metrics = FinancialMetrics.objects.create(
        dettes_financement=dettes_financement,
        dettes_court_terme=dettes_court_terme,
        total_dettes=total_dettes_value,
    )
    return total_dettes_value
