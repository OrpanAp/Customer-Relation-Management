from django.shortcuts import render, redirect
from . import models
from . import forms

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

def lead_create(request):
    form = forms.DrawForm()

    if request.method == "POST":
        form = forms.DrawForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')

    ctx = {
        "form": form,
    }
    return render(request, 'leads/lead_create.html', ctx)


def lead_update(request, pk):
    lead = models.Lead.objects.get(pk=pk)
    form = forms.DrawForm(instance=lead)

    if request.method == "POST":
        form = forms.DrawForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_details', pk=lead.pk)

    ctx = {
        "form": form,
        "pk": lead.pk,
    }
    return render(request, 'leads/lead_update.html', ctx)


def lead_delete(request, pk):
    lead = models.Lead.objects.get(pk=pk)
    lead.delete()
    return redirect('leads:lead_list')