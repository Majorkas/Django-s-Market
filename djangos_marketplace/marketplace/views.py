from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from marketplace.models import MarketItem



class HomeView(ListView):
    model = MarketItem
    template_name = 'marketplace/index.html'
    context_object_name = 'random_items'

    def get_queryset(self):
        # Get 6 random market items that are available
        return MarketItem.objects.filter(
            is_available=True
        ).order_by('?')[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class MarketListView(ListView):
    model = MarketItem
    template_name = 'marketplace/market.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self):
        return MarketItem.objects.filter(is_available=True).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Market'
        return context


class ItemDetailView(DetailView):
    model = MarketItem
    template_name = 'marketplace/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = MarketItem
    fields = ['title', 'description', 'price', 'contact', 'image']
    template_name = 'marketplace/item_form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        messages.success(self.request, 'Your item has been posted!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post Item'
        return context


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MarketItem
    fields = ['title', 'is_available', 'description', 'price', 'contact', 'image', ]
    template_name = 'marketplace/item_form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your item has been updated!')
        return super().form_valid(form)

    def test_func(self):
        # Only allow the item owner to edit
        item = self.get_object()
        return self.request.user == item.seller

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Item'
        return context


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MarketItem
    template_name = 'marketplace/item_confirm_delete.html'
    success_url = reverse_lazy('profile')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Your item has been deleted!')
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        # Only allow the item owner to delete
        item = self.get_object()
        return self.request.user == item.seller

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Item'
        return context
