from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from . import models
from . import forms


# Function based view
""" def home_page(request):
    return render(request, 'leads/home.html')

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
 """

# class based view
class HomeView(TemplateView):
    template_name = "leads/home.html"

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = models.Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "leads/lead_details.html"
    queryset = models.Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = forms.DrawForm

    def get_success_url(self):
        return reverse('leads:lead_list')

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    form_class = forms.DrawForm
    queryset = models.Lead.objects.all()
    context_object_name = "lead"

    def get_success_url(self):
        return reverse('leads:lead_details', kwargs={"pk": self.object.pk})

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = models.Lead.objects.all()
    context_object_name = "lead"

    def get_success_url(self):
        return reverse('leads:lead_list')





