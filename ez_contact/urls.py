from django.conf.urls.defaults import *
from django.views.generic import TemplateView

from ez_contact.views import contact, json_contact

class ContactSuccessView(TemplateView):
    template_name = 'ez_contact/contact-success.html'

urlpatterns = patterns('',
    url(r'json-contact/$', json_contact, name='json-contact'),
    url(r'contact-form/$', contact, name='contact-form-send'),
    url(r'contact-success/$', ContactSuccessView.as_view(), name='contact-form-success'),
)