import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView,
)

# apps entrada
from applications.entrada.models import Entry
# models
from .models import Home
# froms
from .forms import SuscribersForms

class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        # cargamos el home
        context['home'] = Home.objects.latest('created')

        # contexto de portada
        context['portada'] = Entry.objects.entrada_en_portada()

        # contecto para los atículos en home
        context['entradas_home'] = Entry.objects.entradas_en_home()

        # contecto para los atículos en entradas recientes
        context['entradas_recientes'] = Entry.objects.entradas_recientes()

        # envio de formulario de subscripcion
        context['form'] = SuscribersForms

        return context


class SuscriberCreateView(CreateView):
    form_class = SuscribersForms
    success_url = '.'
