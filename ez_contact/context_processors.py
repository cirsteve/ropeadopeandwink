from ez_contact.forms import ContactForm
from recaptcha.client import captcha
from django.conf import settings


def contact_form(request):
    contactform = ContactForm()
    return {'contactform': contactform }