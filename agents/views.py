from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from leads.models import Agent
from . import forms




class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    queryset = Agent.objects.all()
    context_object_name = 'agents'


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class= forms.AgentCreationForm

    def get_success_url(self):
        return reverse('agents:agents')
    
    def form_valid(self, form):
        agent = form.save(commit = False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    

class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_details.html"
    queryset = Agent.objects.all()
    context_object_name = 'agent'
    
class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    queryset = Agent.objects.all()
    context_object_name = 'agent'
    form_class = forms.AgentCreationForm
    
    def get_success_url(self):
        return reverse('agents:agent_details', kwargs={"pk": self.object.pk})
    
class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = Agent.objects.all()
    context_object_name = 'agent'
    
    def get_success_url(self):
        return reverse('agents:agents')
    
    
