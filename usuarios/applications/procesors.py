from applications.home.models import Home

# procesor para recuperar telefono y correo del registro home
def home_contact(request):

    home = Home.objects.latest('created')
    return {
        'phone': home.phone,
        'correo': home.contact_email,
    }
