from django import forms

# models
from .models import Suscribers, Contact


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


class ContactFrom(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('__all__')
