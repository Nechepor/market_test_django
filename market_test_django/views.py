from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class CustomRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/login/'
