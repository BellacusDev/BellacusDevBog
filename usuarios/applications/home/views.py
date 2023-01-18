import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView
)

# apps entrada
from applications.entrada.models import Entry


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        # contexto de portada
        context['portada'] = Entry.objects.entrada_en_portada()

        # contecto para los atículos en home
        context['entradas_home'] = Entry.objects.entradas_en_home()

        # contecto para los atículos en entradas recientes
        context['entradas_recientes'] = Entry.objects.entradas_recientes()

        return context