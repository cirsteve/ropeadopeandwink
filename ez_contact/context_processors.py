from ez_contact.forms import ContactForm

def contact_form(request):
    contactform = ContactForm()
    return {'contactform': contactform }