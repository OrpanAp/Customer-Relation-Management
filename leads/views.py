from django.shortcuts import render, redirect, reverse
from django.views import generic
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizerAndLoginRequiredMixin
from django.core.mail import send_mail


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
class HomeView(generic.TemplateView):
    template_name = "leads/home.html"

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = models.Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            queryset = models.Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            queryset = queryset.filter(agent__user = user)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organizer:
            queryset = models.Lead.objects.filter(
                organization=user.userprofile,
                agent__isnull = True
            )
            
            context.update({
                "unassigned_leads": queryset
            })
        return context
    
    

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_details.html"
    context_object_name = "lead"
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = models.Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = models.Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user = user)
            
        return queryset

class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = forms.DrawForm

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def form_valid(self, form):
        send_mail (
            subject='A new lead has been created',
            message='Visit the new lead in our site',
            from_email='test@mail.com',
            recipient_list=['test2@mail.com']
        )
        return super(LeadCreateView, self).form_valid(form)
    

class LeadUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = forms.DrawForm
    context_object_name = "lead"

    def get_success_url(self):
        return reverse('leads:lead_details', kwargs={"pk": self.object.pk})
    
    def get_queryset(self):
        user = self.request.user
        return models.Lead.objects.filter(organization=user.userprofile)

class LeadDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    context_object_name = "lead"

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def get_queryset(self):
        user = self.request.user
        return models.Lead.objects.filter(organization=user.userprofile)

class RegistrationView(generic.CreateView):
    template_name = "registration/register.html"
    form_class = forms.CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')



class AgentAssignView(OrganizerAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = forms.AssignAgentForm
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AgentAssignView, self).get_form_kwargs(**kwargs)
        kwargs.update({
             "request": self.request
         })
        return kwargs
    
    def get_success_url(self):
        return reverse("leads:lead_list")
    
    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = models.Lead.objects.get(id = self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AgentAssignView, self).form_valid(form)
    
    

class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "categories"
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user
        
        if user.is_organizer:
            queryset = models.Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = models.Lead.objects.filter(organization=user.agent.organization)
            
        
            
        context.update({
            'unassigned_lead_count': queryset.filter(category__isnull = True).count
        }) 
        return context
    
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = models.Category.objects.filter(organization=user.userprofile)
        else:
            queryset = models.Category.objects.filter(organization=user.agent.organization)
            
        return queryset
    
class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/category_details.html"
    context_object_name = "category"
    
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = models.Category.objects.filter(organization=user.userprofile)
        else:
            queryset = models.Category.objects.filter(organization=user.agent.organization)
            
        return queryset
    
    
class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_category_update.html"
    form_class = forms.LeadCategoryUpdateForm
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = models.Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = models.Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user = user)
            
        return queryset
    
    def get_success_url(self):
        return reverse("leads:lead_details", kwargs={ "pk": self.get_object().id })
