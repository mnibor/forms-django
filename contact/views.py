from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

def contact(request):
    # print('Tipo de petición: {}'.format(request.method))
    contact_form = ContactForm()
    
    if request.method == 'POST':
        # Estoy enviando el formulario
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            # Enviar el correo electrónico

            return redirect(reverse('contact')+'?ok')

    return render(request, 'contact/contact.html', {'form':contact_form})