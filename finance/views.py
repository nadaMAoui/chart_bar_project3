from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bilan, Type
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
from django.http import JsonResponse
import json
# Create your views here.

def search_bilan(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        bilan = Bilan.objects.filter(
            actif_immobilisé__istartswith=search_str, owner=request.user) | Bilan.objects.filter(
            stock__istartswith=search_str, owner=request.user) | Bilan.objects.filter(
            créances__istartswith=search_str, owner=request.user) | Bilan.objects.filter(
            trésorerie_actif__istartswith=search_str, owner=request.user) | Bilan.objects.filter(
            capitaux_propre__istartswith=search_str, owner=request.user) | Bilan.objects.filter(
            dette_de_financement__istartswith=search_str, owner=request.user) | Bilan.objects.filter(
            dette_à_court_terme__istartswith=search_str, owner=request.user) | Bilan.objects.filter(
            type__icontains=search_str, owner=request.user(
            date__istartswith=search_str, owner=request.user) | Bilan.objects.filter)
        data = bilan.values()
        return JsonResponse(list(data), safe=False)


@login_required(login_url='/authentication/login')
def index(request):
    types = Type.objects.all()
    bilans = Bilan.objects.filter(owner=request.user)
    paginator = Paginator(bilans, 2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'bilans': bilans,
        'page_obj': page_obj
    }
    return render(request, 'finance/index.html', context)

def add_bilan(request):
    types = Type.objects.all()
    context = {
        'types': types,
        'value': request.POST 
    }
    if request.method == 'GET':
        return render(request, 'finance/add_bilan.html', context)

    if request.method == 'POST':
        actif_immobilisé = request.POST['actif_immobilisé']

        if not actif_immobilisé:
            messages.error(request, 'Actif immobilisé is required')
            return render(request, 'finance/add_bilan.html', context)
        stock = request.POST['stock']
        créances = request.POST['créances']
        trésorerie_actif = request.POST['trésorerie_actif']
        capitaux_propre = request.POST['capitaux_propre']
        dette_de_financement = request.POST['dette_de_financement']
        dette_à_court_terme = request.POST['dette_à_court_terme']
        type = request.POST['type']
        date = request.POST['bilan_date']

        if not stock:
            messages.error(request, 'Stock is required')
            return render(request, 'finance/add_bilan.html', context)
        if not créances:
            messages.error(request, 'Créances is required')
            return render(request, 'finance/add_bilan.html', context)
        if not trésorerie_actif:
            messages.error(request, 'Trésorerie is required')
            return render(request, 'finance/add_bilan.html', context)
        if not capitaux_propre:
            messages.error(request, 'Capitaux propre is required')
            return render(request, 'finance/add_bilan.html', context)
        if not dette_de_financement:
            messages.error(request, 'dette de financement is required')
            return render(request, 'finance/add_bilan.html', context)
        if not dette_à_court_terme:
            messages.error(request, 'Dette à court terme is required')
            return render(request, 'finance/add_bilan.html', context)


        Bilan.objects.create(owner=request.user, actif_immobilisé=actif_immobilisé, stock=stock, créances=créances, trésorerie_actif=trésorerie_actif, capitaux_propre=capitaux_propre, dette_de_financement=dette_de_financement, dette_à_court_terme=dette_à_court_terme, type=type, date=date)

        messages.success(request, 'Bilan saved successffully')

        return redirect('finance')
    

def bilan_edit(request, id):
    bilan = Bilan.objects.get(pk=id)
    types = Type.objects.all()
    context = {
        'bilan' : bilan,
        'values' : bilan,
        'types' : types
    }
    if request.method=='GET':
        return render(request, 'finance/edit-bilan.html', context)
 
    if request.method == 'POST':
        actif_immobilisé = request.POST['actif_immobilisé']

        if not actif_immobilisé:
            messages.error(request, 'Actif immobilisé is required')
            return render(request, 'finance/edit-bilan.html', context)
        stock = request.POST['stock']
        créances = request.POST['créances']
        trésorerie_actif = request.POST['trésorerie_actif']
        capitaux_propre = request.POST['capitaux_propre']
        dette_de_financement = request.POST['dette_de_financement']
        dette_à_court_terme = request.POST['dette_à_court_terme']
        type = request.POST['type']
        date = request.POST['bilan_date']

        if not stock:
            messages.error(request, 'Stock is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not créances:
            messages.error(request, 'Créances is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not trésorerie_actif:
            messages.error(request, 'Trésorerie is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not capitaux_propre:
            messages.error(request, 'Capitaux propre is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not dette_de_financement:
            messages.error(request, 'dette de financement is required')
            return render(request, 'finance/edit-bilan.html', context)
        if not dette_à_court_terme:
            messages.error(request, 'Dette à court terme is required')
            return render(request, 'finance/edit-bilan.html', context)


        bilan.owner = request.user
        bilan.stock = stock
        bilan.créances = créances
        bilan.trésorerie_actif = trésorerie_actif
        bilan.capitaux_propre = capitaux_propre
        bilan.dette_de_financement = dette_de_financement
        bilan.dette_à_court_terme = dette_à_court_terme
        bilan.type = type
        bilan.date = date

        bilan.save()
        messages.success(request, 'Bilan updated  successfully')

        return redirect('finance')

def delete_bilan(request, id):
    bilan = Bilan.objects.get(pk=id)
    bilan.delete()
    messages.success(request, 'Bilan removed')
    return redirect('finance') 


def bilan_summary(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date-datetime.timedelta(days=30*6)
    bilan = Bilan.objects.filter(owner=request.user,
        date__gte=six_months_ago, date_lte=todays_date)
    finalrep = {}

    def get_bilan(bilan):
        actif_immobilisé = int(request.GET["actif_immobilisé"])
        stock = int(request.GET["stock"])
        créances = int(request.GET["créances"])
        trésorerie_actif = int(request.GET["trésorerie_actif"])
        capitaux_propre = int(request.GET["capiatux_propre"])
        dette_de_financement = int(request.GET["dette_de_financement"])
        dette_à_court_terme = int(request.GET["dette_à_court_terme"])
        actif = actif_immobilisé + stock + créances + trésorerie_actif
        passif = capitaux_propre + dette_de_financement + dette_à_court_terme
        fond_de_roulement = (capitaux_propre + dette_de_financement) - dette_à_court_terme
        besoin_de_fond_de_roulement = (stock + créances) - dette_à_court_terme
        trésorerie_net =  fond_de_roulement - besoin_de_fond_de_roulement 
        financement_permanent = (capitaux_propre + dette_de_financement) / actif_immobilisé
        autonomie_financiére = capitaux_propre / financement_permanent
        solvabilité_genérale = actif / (dette_à_court_terme + dette_de_financement)
        capacité_de_remboursement = capitaux_propre / dette_de_financement
        return (request, {"Actif": actif}, {"Passif": passif}, {"Fond de roulement": fond_de_roulement }, {"Besoin de fond de roulement": besoin_de_fond_de_roulement},
                     {"trésorerie_net"}, {"financement permanent" : financement_permanent}, {"Autonomie financiére": autonomie_financiére},
                     {"solvabilité genérale": solvabilité_genérale}, {"Capacité de remboursement": capacité_de_remboursement})
    finalrep = get_bilan(bilan)
    return JsonResponse({"data_bilan":finalrep})

def stats_view(request):
    return render(request, 'finance/stats.html')