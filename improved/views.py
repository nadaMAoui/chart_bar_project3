from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bilan, Type
from django.core.paginator import Paginator

# Create your views here.

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
        form_fields = ['actif_immobilisé', 'stock', 'créances', 'trésorerie_actif', 'capitaux_propre', 'dette_de_financement', 'dette_à_court_terme', 'type', 'bilan_date']
        form_values = {field: request.POST.get(field) for field in form_fields}

        for field, value in form_values.items():
            if not value:
                messages.error(request, f'{field.replace("_", " ").title()} is required')
                return render(request, 'finance/add_bilan.html', context)
        
        Bilan.objects.create(owner=request.user, **form_values)
        messages.success(request, 'Bilan saved successfully')
        return redirect('finance')

def bilan_edit(request, id):
    bilan = Bilan.objects.get(pk=id)
    types = Type.objects.all()
    context = {
        'bilan': bilan,
        'values': bilan,
        'types': types
    }
    if request.method == 'GET':
        return render(request, 'finance/edit-bilan.html', context)
    
    if request.method == 'POST':
        form_fields = ['actif_immobilisé', 'stock', 'créances', 'trésorerie_actif', 'capitaux_propre', 'dette_de_financement', 'dette_à_court_terme', 'type', 'bilan_date']
        form_values = {field: request.POST.get(field) for field in form_fields}

        for field, value in form_values.items():
            if not value:
                messages.error(request, f'{field.replace("_", " ").title()} is required')
                return render(request, 'finance/edit-bilan.html', context)
        
        bilan.__dict__.update(**form_values)
        bilan.save()
        messages.success(request, 'Bilan updated successfully')
        return redirect('finance')

def delete_bilan(request, id):
    bilan = Bilan.objects.get(pk=id)
    bilan.delete()
    messages.success(request, 'Bilan removed')
    return redirect('finance')
