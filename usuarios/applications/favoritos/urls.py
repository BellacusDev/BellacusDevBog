from django.urls import path
from . import views

app_name='favoritos_app'

urlpatterns = [
    path(
        'perfil',
        views.UserPageView.as_view(),
        name='perfil',
    ),
]