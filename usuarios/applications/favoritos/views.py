from django.shortcuts import render
#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    View,
)
from applications.entrada.models import Entry
from .models import Favorites
# Create your views here.


class UserPageView(LoginRequiredMixin, ListView):
    template_name = 'favoritos/perfil.html'
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)


class AddFavoritesView(View):

    def post(self, request, *args, **kwargs):

        # recuperar usuario
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])

        # registramos favoritos
        Favorites.objects.create(
            user=usuario,
            entry=entrada,
        )

        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil',
            )
        )
