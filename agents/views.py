from django.shortcuts import render, reverse
# from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganizerAndLoginRequiredMixin
from django.views import generic
from leads.models import Agent
from . import forms
from django.core.mail import send_mail



class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = 'agents'
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    

class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class= forms.AgentCreationForm

    def get_success_url(self):
        return reverse('agents:agents')
    
    def form_valid(self, form):
        user = form.save(commit = False)
        user.is_agent = True
        user.is_organizer = False
        user.set_unusable_password()
        user.save()
        
        Agent.objects.create(
            user = user,
            organization = self.request.user.userprofile,
        )
        
        send_mail(
            subject= "You were added as an agent.",
            message= "Please visit our site and start working",
            from_email= "admin@mail.com",
            recipient_list=[user.email]
        )
        
        return super(AgentCreateView, self).form_valid(form)
    

class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_details.html"
    context_object_name = 'agent'
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    context_object_name = 'agent'
    form_class = forms.AgentCreationForm
    
    def get_queryset(self):
        return Agent.objects.filter(organization= self.request.user.userprofile)
    
    def get_success_url(self):
        return reverse('agents:agent_details', kwargs={"pk": self.object.pk})
    
class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = 'agent'
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
    
    def get_success_url(self):
        return reverse('agents:agents')