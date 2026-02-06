from django.shortcuts import render
from . import models

def home_page(request):
    leads = models.Lead.objects.all()
    ctx = {
        "leads": leads,
    }
    return render(request, 'home.html', ctx)

def lead_list(request):
    leads = models.Lead.objects.all()
    ctx = {
        "leads": leads,
    }
    return render(request, 'leads/lead_list.html', ctx)

def lead_details(request, pk):
    lead = models.Lead.objects.get(pk=pk)
    ctx = {
        "lead": lead,
    }
    return render(request, 'leads/lead_details.html', ctx)