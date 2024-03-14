from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Announce, Category, Respond
from .forms import AnnounceForm, RespondForm


# Create your views here.
# def home_page(request):
#     return render(request, 'flatpages/index.html')


class AnnounceListView(ListView):
    model = Announce
    ordering = '-time_to_update'
    template_name = 'announces_list.html'
    context_object_name = 'announces_list'


class AnnounceDetailView(DetailView):
    model = Announce
    template_name = 'announce_detail.html'
    context_object_name = 'announce_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RespondForm
        return context


class AnnounceCreateView(LoginRequiredMixin, CreateView):
    model = Announce
    template_name = 'create_announce.html'
    form_class = AnnounceForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class AnnounceUpdateView(LoginRequiredMixin, UpdateView):
    model = Announce
    template_name = 'create_announce.html'
    form_class = AnnounceForm

    # def get_form_kwargs(self):
    #     kwargs = super(AnnounceUpdateView, self).get_form_kwargs()
    #     #kwargs.update({'user': self.request.user})
    #     kwargs['user'] = self.request.user
    #     return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_object(self, **kwargs):
        slug = self.kwargs.get('slug')
        return Announce.objects.get(slug=slug)


class AnnounceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_announce.html'
    queryset = Announce.objects.all()
    context_object_name = 'announce'
    success_url = reverse_lazy('announcies_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories_list'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category_detail'


class RespondCreateView(LoginRequiredMixin, CreateView):
    model = Respond
    form_class = RespondForm
    #template_name = 'respond_create.html'

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        respond = form.save(commit=False)
        respond.author = self.request.user
        respond.announce_id = self.kwargs.get('pk')
        respond.save()

        return redirect(respond.announce.get_absolute_url())
