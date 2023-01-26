from django import forms

# models
from .models import Suscribers


class SuscribersForms(forms.ModelForm):

    class Meta:
        model = Suscribers
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electrónico...'
                }
            )
        }