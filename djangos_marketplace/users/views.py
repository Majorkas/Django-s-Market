from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import UserProfileForm
from .models import UserProfile
from marketplace.models import MarketItem


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Return the profile of the currently logged-in user
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'

        # Get all market items posted by the user split by if available or not
        context['available_items'] = MarketItem.objects.filter(
            seller=self.request.user,
            is_available=True
        ).order_by('-date_posted')

        context['unavailable_items'] = MarketItem.objects.filter(
            seller=self.request.user,
            is_available=False
        ).order_by('-date_posted')

        return context
