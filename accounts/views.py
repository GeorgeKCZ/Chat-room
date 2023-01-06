from logging import getLogger

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

LOGGER = getLogger()

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('rooms')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        username = cleaned_data['username']
        password = cleaned_data['password1']
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
             login(self.request, new_user)

        LOGGER.warning(new_user)
        return result

