from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Announce, Category, Respond
from .forms import AnnounceForm


# Create your views here.
def home_page(request):
    return render(request, 'flatpages/index.html')


class AnnounceListView(ListView):
    model = Announce
    ordering = '-time_to_update'
    template_name = 'allannoun.html'
    context_object_name = 'announce_list'


class AnnounceDetailView(DetailView):
    model = Announce
    template_name = 'announ_detail.html'
    context_object_name = 'announ_detail'


class AnnounceCreateView(CreateView):
    model = Announce
    template_name = 'create_announ.html'
    form_class = AnnounceForm

    def get_form_kwargs(self):
        kwargs = super(AnnounceCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
