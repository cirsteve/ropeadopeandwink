from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from ez_contact.forms import ContactForm

from entry.views import EntryListView

class HomeView(TemplateView):
    template_name = "home.html"
    
class WhereView(TemplateView):
    template_name = "where.html"
    
class LabsView(TemplateView):
    template_name = "labs_home.html"
    
class BioView(TemplateView):
    template_name = 'bio.html'
    
    def get_context_data(self, **kwargs):
        context = super(BioView, self).get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rdw.views.home', name='home'),
    # url(r'^rdw/', include('rdw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # from django.contrib.staticfiles.urls import staticfiles_urlpatternsUncomment the next line to enable the admin:
    url(r'^steven-ciraolo/$', BioView.as_view(), name='bio.html'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^contact/', include('ez_contact.urls')),
    url(r'^blog/', include('entry.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ropeadope/$', HomeView.as_view(), name="home"),
    url(r'^labs/$', LabsView.as_view(), name="labs"),
    url(r'^labs/where/$', WhereView.as_view(), name="where"),
    url(r'^$', EntryListView.as_view()),
)
